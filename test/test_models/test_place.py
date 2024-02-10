#!/usr/bin/python3

import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_instance_creation(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes(self):
        place = Place()
        place.city_id = "1234"
        place.user_id = "5678"
        place.name = "Test Place"
        place.description = "Test Description"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["a1", "a2"]
        self.assertEqual(place.city_id, "1234")
        self.assertEqual(place.user_id, "5678")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "Test Description")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["a1", "a2"])

    def test_inherited_methods(self):
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "to_dict"))
        self.assertTrue(hasattr(place, "save"))

    def test_to_dict(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)
        self.assertEqual(place_dict['city_id'], "")
        self.assertEqual(place_dict['user_id'], "")
        self.assertEqual(place_dict['name'], "")
        self.assertEqual(place_dict['description'], "")
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])


if __name__ == '__main__':
    unittest.main()
