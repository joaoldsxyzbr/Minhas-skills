"""Replay native JS behavior checks; requires installed Node, never installs it."""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]

@unittest.skipUnless(shutil.which('node'),'Node unavailable: JS behavior not verified')
class BehaviorChecks(unittest.TestCase):
    def test_documented_retry_example(self):
        text=(ROOT/'skills/test-driven-development/SKILL.md').read_text()
        blocks=re.findall(r'```javascript\n(.*?)\n```',text,re.S)
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)
            (p/'retry.mjs').write_text(blocks[1]+'\n')
            (p/'retry.test.mjs').write_text(blocks[0]+'''\n
test('immediate success calls once', async () => {
  let calls=0;
  assert.equal(await retryOperation(async()=>{calls++;return 7;}),7);
  assert.equal(calls,1);
});
test('last rejection is propagated after three attempts', async () => {
  let calls=0; const error=new Error('permanent');
  await assert.rejects(retryOperation(async()=>{calls++;throw error;}),e=>e===error);
  assert.equal(calls,3);
});
''')
            r=subprocess.run(['node','--test','retry.test.mjs'],cwd=p,capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stdout+r.stderr)
    def test_import_regression_red_green_replay(self):
        fixture=ROOT/'tests/fixtures/import'
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder);shutil.copyfile(fixture/'import.test.mjs',p/'import.test.mjs')
            shutil.copyfile(fixture/'before.mjs',p/'import.mjs')
            red=subprocess.run(['node','--test','import.test.mjs'],cwd=p,capture_output=True,text=True)
            self.assertNotEqual(red.returncode,0,'regression suite failed to catch original defect')
            self.assertIn('AssertionError',red.stdout+red.stderr,'not an assertion failure')
            shutil.copyfile(fixture/'after.mjs',p/'import.mjs')
            green=subprocess.run(['node','--test','import.test.mjs'],cwd=p,capture_output=True,text=True)
            self.assertEqual(green.returncode,0,green.stdout+green.stderr)

if __name__=='__main__':unittest.main()
