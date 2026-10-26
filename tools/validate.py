"""Offline maintainer checks and packaging; Python standard library only.
This validates structure, not semantic routing or host activation.
"""
import argparse
import json
from pathlib import Path
import re
import zipfile

ROOT_FILES = ('plugin.json', 'README.md', 'PRIVACY.md', 'PLUGIN_PACKAGE.md',
              'THIRD_PARTY_NOTICES.md', 'LICENSE-SUPERPOWERS.txt', 'LICENSE-CLOUDFLARE.txt')

def metadata(text):
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('missing frontmatter')
    header, body = text[4:].split('\n---\n', 1)
    fields = {}
    for line in header.splitlines():
        key, sep, value = line.partition(': ')
        if not sep or key not in ('name', 'description') or key in fields:
            raise ValueError('expected unique name/description scalar fields')
        if value.startswith('"'):
            value = json.loads(value)
        elif not re.fullmatch(r'[A-Za-z0-9][^:#\n]*', value):
            raise ValueError('quote YAML punctuation with a JSON-compatible string')
        if not isinstance(value, str) or not value.strip():
            raise ValueError('non-empty string required')
        fields[key] = value
    if set(fields) != {'name', 'description'} or not body.strip():
        raise ValueError('incomplete skill')
    return fields

def unfenced(text):
    return re.sub(r'(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text)

def anchors(text):
    result, counts = set(), {}
    for title in re.findall(r'(?m)^#{1,6}\s+(.+?)(?:\s+#+)?$', unfenced(text)):
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        n = counts.get(slug, 0); counts[slug] = n + 1
        result.add(slug + (f'-{n}' if n else ''))
    return result

def validate(root):
    root = Path(root).resolve()
    errors=[]
    def check(condition, message):
        if not condition: errors.append(message)
    try:
        manifest=json.loads((root/'plugin.json').read_text())
        check(isinstance(manifest,dict), 'manifest must be an object')
        if not isinstance(manifest,dict): return errors
        check(manifest.get('$schema')=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json','manifest schema')
        check(manifest.get('name')=='minhas-skills','plugin identity changed')
        check(bool(re.fullmatch(r'\d+\.\d+\.\d+', str(manifest.get('version','')))),'strict release version')
        check(not any(k in manifest for k in ('skills','mcpServers','apps','interface')), 'portable manifest has legacy fields')
        interface=manifest['extensions']['com.openai']['interface']
        check(0<len(interface['shortDescription'])<=30,'subtitle length')
        check(interface['displayName']=='Minhas Skills','display name changed')
        check(isinstance(interface.get('capabilities'),list),'capabilities must be a list')
        check('apps' not in manifest['extensions']['com.openai'],'unexpected connected app')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append('invalid manifest: '+str(exc))
    skills=sorted((root/'skills').glob('*/SKILL.md'))
    check(bool(skills), 'at least one skill is required')
    names=set()
    for path in skills:
        try:
            text=path.read_text(); fields=metadata(text); name=fields['name']
            check(name==path.parent.name and bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name)),f'{path}: name/folder mismatch')
            check(name not in names,f'duplicate skill: {name}');names.add(name)
            check(len(text.encode())<=1024*1024,f'{path}: too large')
            check(len(text.splitlines())<500,f'{path}: split conditional references')
        except (OSError,ValueError) as exc: errors.append(f'{path}: {exc}')
    for path in (root/'skills').rglob('*'):
        if path.is_symlink():
            errors.append(f'symlink in skills: {path}'); continue
        if path.is_file():
            check(path.name!='SKILL.md' or len(path.relative_to(root).parts)==3,f'undiscoverable nested skill: {path}')
            check(path.suffix=='.md',f'unexpected runtime payload: {path}')
            text=path.read_text()
            check(not re.search(r'superpowers:|cf-cli skill|subagent-driven-development',text,re.I),f'{path}: external skill route')
    for path in [*(root/'skills').rglob('*.md'),*[root/f for f in ROOT_FILES if f.endswith('.md')]]:
        if not path.exists():errors.append(f'missing required file: {path}');continue
        for dest in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',unfenced(path.read_text())):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',dest):
                check(dest.startswith('https://'),f'{path}: unsafe link scheme: {dest}')
                continue
            local,_,anchor=dest.partition('#')
            target=(path.parent/local).resolve() if local else path.resolve()
            check(target.is_relative_to(root),f'{path}: link escapes package: {dest}')
            check(target.is_file(),f'{path}: missing link target: {dest}')
            if anchor and target.is_file():
                check(anchor in anchors(target.read_text()),f'{path}: missing anchor: {dest}')
    for f in ('mcp.json','.mcp.json','.app.json'):
        check(not (root/f).exists(),f'unexpected connected component: {f}')
    for f in ROOT_FILES:
        check((root/f).is_file(),f'missing package file: {f}')
        check(not (root/f).is_symlink(),f'symlink package file: {f}')
    return errors

def package(root, destination):
    root=Path(root).resolve();destination=Path(destination).resolve()
    if destination.is_relative_to(root): raise ValueError('archive must be outside source directory')
    errors=validate(root)
    if errors: raise ValueError('\n'.join(errors))
    paths=[root/f for f in ROOT_FILES]+sorted((root/'skills').rglob('*.md'))
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as z:
        for path in paths:z.write(path,path.relative_to(root).as_posix())
    with zipfile.ZipFile(destination) as z:
        if z.testzip() is not None: raise ValueError('ZIP integrity failure')
        if len(z.namelist())!=len(set(z.namelist())): raise ValueError('duplicate archive entries')
    return len(paths)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--archive',type=Path)
    args=parser.parse_args();errors=validate(args.root)
    if errors:
        print('\n'.join(errors));return 1
    print(f'PASS: manifest, {len(list((args.root / "skills").glob("*/SKILL.md")))} skill headers, local links/anchors, package boundaries and payload policy')
    if args.archive:print(f'PASS: {package(args.root,args.archive)} packaged files; ZIP integrity checked')
    return 0

if __name__=='__main__':raise SystemExit(main())
