#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_instance_creation(self):
        obj = State()
        self.assertIsInstance(obj, State)

    def test_default_attributes(self):
        obj = State()
        self.assertEqual(obj.name, "")


if __name__ == '__main__':
    unittest.main()
