import unittest
import os

from core.logic_engine import AHKSZ_Core
from guardian.guardian_protocols import check_ethics
from muscle.action_handler import perform_action
from senses.sensor_hub import scan_environment


class TestCore(unittest.TestCase):
    def test_process_input(self):
        core = AHKSZ_Core()
        out = core.process_input('test')
        self.assertIn('AHKSZ says', out)


class TestGuardian(unittest.TestCase):
    def test_ethics_blocks(self):
        self.assertFalse(check_ethics('we should kill them'))
        self.assertTrue(check_ethics('hello world'))


class TestMuscle(unittest.TestCase):
    def test_perform_action(self):
        res = perform_action('echo unit-test')
        self.assertIn('unit-test', res)


class TestSenses(unittest.TestCase):
    def test_scan_env(self):
        env = scan_environment()
        self.assertIsInstance(env, dict)


if __name__ == '__main__':
    unittest.main()
