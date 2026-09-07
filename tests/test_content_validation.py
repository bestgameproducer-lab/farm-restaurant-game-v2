"""Negative fixtures for the bootstrap validator; does not pretend to test Godot."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate_content', ROOT / 'tools/validate_content.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ContentValidationTests(unittest.TestCase):
    def setUp(self):
        folder = ROOT / 'content/employees'
        self.catalog, self.definitions, self.knowledge = [json.loads((folder / n).read_text()) for n in ('catalog.json', 'definitions.json', 'knowledge.json')]
    def errors(self):
        return module.validate(self.catalog, self.definitions, self.knowledge)
    def test_valid(self):
        self.assertEqual(self.errors(), [])
    def test_duplicate_id(self):
        self.definitions['employees'].append(copy.deepcopy(self.definitions['employees'][0]))
        self.assertTrue(self.errors())
    def test_unknown_profession(self):
        self.definitions['employees'][0]['profession_id'] = 'unknown'
        self.assertTrue(self.errors())
    def test_unknown_trait(self):
        self.definitions['employees'][0]['traits'].append('unknown')
        self.assertTrue(self.errors())
    def test_negative_wage(self):
        self.definitions['employees'][0]['wage_per_service'] = -1
        self.assertTrue(self.errors())
    def test_nan_skill(self):
        self.definitions['employees'][0]['skills']['service'] = float('nan')
        self.assertTrue(self.errors())
    def test_boolean_skill(self):
        self.definitions['employees'][0]['skills']['service'] = True
        self.assertTrue(self.errors())
    def test_skill_overflow(self):
        self.definitions['employees'][0]['skills']['service'] = 101
        self.assertTrue(self.errors())
    def test_orphan_profile(self):
        self.knowledge['profiles'][0]['employee_id'] = 'nobody'
        self.assertTrue(self.errors())
    def test_missing_profile(self):
        self.knowledge['profiles'].pop()
        self.assertTrue(self.errors())
    def test_hidden_truth_leak(self):
        self.knowledge['profiles'][0]['observations'][1]['value'] = 12
        self.assertTrue(self.errors())
    def test_reversed_estimate(self):
        self.knowledge['profiles'][1]['observations'][0]['range'] = [90, 60]
        self.assertTrue(self.errors())
    def test_estimate_may_be_wrong(self):
        self.knowledge['profiles'][1]['observations'][0]['range'] = [10, 20]
        self.assertEqual(self.errors(), [])
    def test_false_resume_is_allowed(self):
        self.assertNotEqual(self.definitions['employees'][3]['title_id'], self.knowledge['profiles'][3]['claims'][0]['claimed_value'])
        self.assertEqual(self.errors(), [])
    def test_verified_mismatch(self):
        self.knowledge['profiles'][0]['observations'][0]['value'] = 99
        self.assertTrue(self.errors())
    def test_private_profile_field(self):
        self.knowledge['profiles'][0]['private_goal'] = 'become_chef'
        self.assertTrue(self.errors())

if __name__ == '__main__':
    unittest.main()
