#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        """Test if Amenity instance has the required attributes"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_default_values(self):
        """Test if default values are set correctly"""
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method of Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_str(self):
        """Test the __str__ method of Amenity"""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_update_attribute(self):
        """Test updating an attribute of Amenity"""
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")
        self.amenity.save()
        self.assertIn('name', self.amenity.to_dict())
        self.assertEqual(self.amenity.to_dict()['name'], "Pool")


if __name__ == '__main__':
    unittest.main()
