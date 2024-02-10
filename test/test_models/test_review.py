#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def test_instance_creation(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsNotNone(review.id)

    def test_to_dict(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")
        self.assertEqual(
            review_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(
            review_dict['updated_at'], review.updated_at.isoformat())

    def test_str_representation(self):
        review = Review()
        str_repr = str(review)
        self.assertIn("[Review]", str_repr)
        self.assertIn("'id':", str_repr)
        self.assertIn("'created_at':", str_repr)
        self.assertIn("'updated_at':", str_repr)
        self.assertIn("'place_id':", str_repr)
        self.assertIn("'user_id':", str_repr)
        self.assertIn("'text':", str_repr)


if __name__ == '__main__':
    unittest.main()
