#!/usr/bin/env python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        # Test if BaseModel is correctly initialized with default values.
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_init_with_kwargs(self):
        # Test if BaseModel is correctly initialized with keyword arguments.
        data = {
            "id": "12345",
            "created_at": "2023-01-01T12:00:00",
            "updated_at": "2023-01-02T14:30:00",
            "name": "Test Model"
        }
        my_model = BaseModel(**data)
        self.assertEqual(my_model.id, "12345")
        self.assertEqual(my_model.created_at,
            datetime.fromisoformat("2023-01-01T12:00:00"))
        self.assertEqual(my_model.updated_at,
            datetime.fromisoformat("2023-01-02T14:30:00"))
        self.assertEqual(my_model.name, "Test Model")

    def test_str(self):
        # Test if the string representation of BaseModel is as expected.
        my_model = BaseModel(id="test_id", created_at="2023-01-01T12:00:00")
        expected_str = "[BaseModel] (test_id {'id': 'test_id',
        'created_at': datetime.datetime(2023, 1, 1, 12, 0)})"
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        # Test if the save method updates the updated_at attribute.
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        # Test if the to_dict method returns the expected dictionary.
        data = {
            "id": "12345",
            "created_at": "2023-01-01T12:00:00",
            "updated_at": "2023-01-02T14:30:00",
            "name": "Test Model"
        }
        my_model = BaseModel(**data)
        expected_dict = {
            'id': '12345',
            'created_at': '2023-01-01T12:00:00',
            'updated_at': '2023-01-02T14:30:00',
            'name': 'Test Model',
            '__class__': 'BaseModel'
        }
        self.assertEqual(my_model.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
