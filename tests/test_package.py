"""Validate broken-artifact detection; no third-party dependencies."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',ROOT/'tools/validate.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'plugin';self.root.mkdir()
        for f in v.ROOT_FILES:shutil.copyfile(ROOT/f,self.root/f)
        shutil.copytree(ROOT/'skills',self.root/'skills')
    def test_nested_skill_rejected(self):
        p=self.root/'skills/product-design/nested/SKILL.md';p.parent.mkdir()
        p.write_text('---\nname: nested\ndescription: example\n---\nBody\n')
        self.assertTrue(any('undiscoverable nested' in e for e in v.validate(self.root)))
    def test_symlink_rejected(self):
        p=self.root/'skills/product-design/outside.md';p.symlink_to(self.root/'README.md')
        self.assertTrue(any('symlink in skills' in e for e in v.validate(self.root)))
    def test_valid_package(self):self.assertEqual(v.validate(self.root),[])
    def test_additional_skill_is_allowed(self):
        p=self.root/'skills/another-skill/SKILL.md';p.parent.mkdir()
        p.write_text('---\nname: another-skill\ndescription: Extra supported skill\n---\n\n# Another skill\n')
        self.assertEqual(v.validate(self.root),[])
    def test_examples_in_other_languages_are_allowed(self):
        p=self.root/'skills/product-design/SKILL.md'
        p.write_text(p.read_text()+'\n```rust\nfn main() {}\n```\n```typescript\nconst count: number = 2;\n```\n')
        self.assertEqual(v.validate(self.root),[])
    def test_broken_local_target(self):
        p=self.root/'skills/product-design/SKILL.md';p.write_text(p.read_text()+'\n[missing](gone.md)\n')
        self.assertTrue(any('missing link target' in e for e in v.validate(self.root)))
    def test_broken_anchor(self):
        p=self.root/'skills/product-design/SKILL.md';p.write_text(p.read_text()+'\n[missing](SKILL.md#no-such-heading)\n')
        self.assertTrue(any('missing anchor' in e for e in v.validate(self.root)))
    def test_name_mismatch(self):
        p=self.root/'skills/product-design/SKILL.md';p.write_text(p.read_text().replace('name: product-design','name: other'))
        self.assertTrue(any('mismatch' in e for e in v.validate(self.root)))
    def test_malformed_frontmatter(self):
        with self.assertRaises(ValueError):v.metadata('---\nname: a\ndescription: unquoted: text\n---\nbody')
    def test_payload_rejected(self):
        (self.root/'skills/product-design/tracker.js').write_text('fetch("https://example.invalid")')
        self.assertTrue(any('unexpected runtime payload' in e for e in v.validate(self.root)))
    def test_external_skill_rejected(self):
        p=self.root/'skills/product-design/SKILL.md';p.write_text(p.read_text()+'\nUse superpowers:brainstorming\n')
        self.assertTrue(any('external skill route' in e for e in v.validate(self.root)))
    def test_connected_component_rejected(self):
        (self.root/'mcp.json').write_text('{}')
        self.assertTrue(any('unexpected connected component' in e for e in v.validate(self.root)))
    def test_path_escape_rejected(self):
        p=self.root/'skills/product-design/SKILL.md';p.write_text(p.read_text()+'\n[outside](../../../../secret.md)\n')
        self.assertTrue(any('escapes package' in e for e in v.validate(self.root)))
    def test_archive_whitelist_and_integrity(self):
        (self.root/'private.txt').write_text('not packaged')
        dest=Path(self.temp.name)/'release.zip';v.package(self.root,dest)
        with zipfile.ZipFile(dest) as z:
            self.assertNotIn('private.txt',z.namelist());self.assertIsNone(z.testzip())
            self.assertEqual(sum(n.endswith('/SKILL.md') for n in z.namelist()),len(list((ROOT/'skills').glob('*/SKILL.md'))))
            self.assertFalse(any(n.startswith(('tools/','tests/','.git/')) for n in z.namelist()))
            extracted=Path(self.temp.name)/'extracted';z.extractall(extracted)
            self.assertEqual(v.validate(extracted),[])
    def test_archive_inside_source_rejected(self):
        with self.assertRaises(ValueError):v.package(self.root,self.root/'release.zip')
    def test_fenced_example_is_not_a_file_link(self):
        p=self.root/'skills/product-design/SKILL.md';p.write_text(p.read_text()+'\n```markdown\n[template](placeholder.md)\n```\n')
        self.assertEqual(v.validate(self.root),[])

if __name__=='__main__':unittest.main()
