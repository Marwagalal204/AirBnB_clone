#!/usr/bin/python3
"""unittests for file_storage.py."""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from unittest.mock import patch


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    @patch('builtins.open')
    def test_save(self, mock_open):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        mock_open.assert_called_once_with("file.json", 'w')
        mock_open.return_value.__enter__.return_value.write.assert_called_once()

    @patch('builtins.open')
    def test_reload(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = '{"BaseModel.12345": {"id": "12345", "name": "Test"}}'
        self.storage.reload()
        self.assertIn("BaseModel.12345", self.storage.all())

    @patch('builtins.open')
    def test_reload_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)


if __name__ == '__main__':
    unittest.main()
