import pathlib
import tomllib
import unittest
import re

ROOT=pathlib.Path(__file__).resolve().parents[1]
SKILL=ROOT/'.agents/skills/adaptive-agent-orchestration/SKILL.md'

class PackageTests(unittest.TestCase):
    def test_skill_frontmatter(self):
        s=SKILL.read_text(encoding='utf-8')
        self.assertTrue(s.startswith('---\n'))
        head=s.split('---',2)[1]
        self.assertRegex(head,r'(?m)^name: adaptive-agent-orchestration$')
        self.assertRegex(head,r'(?m)^description: .+$')

    def test_all_local_skill_references_exist(self):
        s=SKILL.read_text(encoding='utf-8')
        links=re.findall(r'\]\((references/[^)]+\.md)\)',s)
        self.assertGreaterEqual(len(links),4)
        for rel in links:
            with self.subTest(rel=rel):
                self.assertTrue((SKILL.parent/rel).is_file())

    def test_agents_toml(self):
        agents=list((ROOT/'agents').glob('*.toml'))
        self.assertGreaterEqual(len(agents),3)
        for path in agents:
            with self.subTest(path=path.name):
                data=tomllib.loads(path.read_text(encoding='utf-8'))
                for required in ('name','description','developer_instructions','model','model_reasoning_effort'):
                    self.assertTrue(data.get(required),f'{path.name}: {required}')
                self.assertIn('ATTEMPTS_AND_ERRORS',data['developer_instructions'])
                self.assertIn('UNRUN_OR_FAILED_CHECKS',data['developer_instructions'])
                self.assertIn('NEEDS_MAIN_AGENT_DECISION',data['developer_instructions'])

    def test_optional_config_parses(self):
        cfg=tomllib.loads((ROOT/'examples/config-snippet.toml').read_text(encoding='utf-8'))
        self.assertEqual(cfg['agents']['max_concurrent_threads_per_session'],3)

    def test_private_project_not_bundled(self):
        names=[str(x.relative_to(ROOT)).lower() for x in ROOT.rglob('*')]
        for ban in ('superbox','wiresock','imei','antigravity_kaynaklar'):
            self.assertFalse(any(ban in x for x in names))

if __name__=='__main__':unittest.main()
