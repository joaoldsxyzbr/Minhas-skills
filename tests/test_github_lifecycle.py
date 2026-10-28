"""Structural checks for the GitHub-centered workflow (not agent behavior tests)."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class GithubLifecycleTests(unittest.TestCase):
    def test_router_and_github_skill_link_to_shared_workflow(self):
        reference = ROOT / 'skills/using-minhas-skills/references/github-lifecycle.md'
        self.assertTrue(reference.is_file())
        self.assertIn('github-lifecycle.md', (ROOT / 'skills/using-minhas-skills/SKILL.md').read_text())
        self.assertIn('github-lifecycle.md', (ROOT / 'skills/github-workflows/SKILL.md').read_text())
        self.assertIn('github-lifecycle.md', (ROOT / 'skills/using-minhas-skills/references/workflow-rules.md').read_text())

    def test_safety_and_resume_paths_are_documented(self):
        workflow = (ROOT / 'skills/using-minhas-skills/references/github-lifecycle.md').read_text()
        for phrase in ('"continue"', 'Issues', 'GitHub Actions', 'Merge, deploy, release', 'not-run', 'plan-only'):
            self.assertIn(phrase, workflow)

if __name__ == '__main__':
    unittest.main()
