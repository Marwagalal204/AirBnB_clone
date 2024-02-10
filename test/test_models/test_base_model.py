#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_generation(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_representation(self):
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)


if __name__ == '__main__':
    unittest.main()
