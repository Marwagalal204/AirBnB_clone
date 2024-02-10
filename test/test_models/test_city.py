#!/usr/bin/python3

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_instance_creation(self):
        self.assertTrue(isinstance(self.city, City))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attributes(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_representation(self):
        string = str(self.city)
        self.assertEqual(string[:11], "[<class City]")
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)
        self.assertIn("'state_id': ''", string)
        self.assertIn("'name': ''", string)

    def test_save_method(self):
        prev_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(prev_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["state_id"], "")
        self.assertEqual(city_dict["name"], "")
        self.assertTrue("id" in city_dict)
        self.assertTrue("created_at" in city_dict)
        self.assertTrue("updated_at" in city_dict)

    def test_to_dict_with_params_method(self):
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)
        self.assertEqual(self.city.state_id, new_city.state_id)
        self.assertEqual(self.city.name, new_city.name)


if __name__ == "__main__":
    unittest.main()
