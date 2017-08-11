import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
from controller import Controller


class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.con = Controller()

    def test_object_creation(self):
        assert(isinstance(self.con, Controller))
