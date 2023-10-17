#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
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


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        baseM = BaseModel()
        user = User()
        STATE = State()
        PLACE = Place()
        town_city = City()
        AMENITY = Amenity()
        REVIEW = Review()
        models.storage.new(baseM)
        models.storage.new(user)
        models.storage.new(STATE)
        models.storage.new(PLACE)
        models.storage.new(town_city)
        models.storage.new(AMENITY)
        models.storage.new(REVIEW)
        self.assertIn("BaseModel." + baseM.id, models.storage.all().keys())
        self.assertIn(baseM, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + STATE.id, models.storage.all().keys())
        self.assertIn(STATE, models.storage.all().values())
        self.assertIn("Place." + PLACE.id, models.storage.all().keys())
        self.assertIn(PLACE, models.storage.all().values())
        self.assertIn("City." +town_city .id, models.storage.all().keys())
        self.assertIn(town_city, models.storage.all().values())
        self.assertIn("Amenity." + AMENITY.id, models.storage.all().keys())
        self.assertIn(AMENITY, models.storage.all().values())
        self.assertIn("Review." + REVIEW.id, models.storage.all().keys())
        self.assertIn(REVIEW, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        baseM = BaseModel()
        user = User()
        STATE = State()
        PLACE = Place()
        town_city = City()
        AMENITY = Amenity()
        REVIEW = Review()
        models.storage.new(baseM)
        models.storage.new(user)
        models.storage.new(STATE)
        models.storage.new(PLACE)
        models.storage.new(town_city)
        models.storage.new(AMENITY)
        models.storage.new(REVIEW)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + baseM.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + STATE.id, save_text)
            self.assertIn("Place." + PLACE.id, save_text)
            self.assertIn("City." + town_city.id, save_text)
            self.assertIn("Amenity." + AMENITY.id, save_text)
            self.assertIn("Review." + REVIEW.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        baseM = BaseModel()
        user = User()
        STATE = State()
        PLACE = Place()
        town_city = City()
        AMENITY = Amenity()
        REVIEW = Review()
        models.storage.new(baseM)
        models.storage.new(user)
        models.storage.new(STATE)
        models.storage.new(PLACE)
        models.storage.new(town_city)
        models.storage.new(AMENITY)
        models.storage.new(REVIEW)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." +baseM.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + STATE.id, objs)
        self.assertIn("Place." + PLACE.id, objs)
        self.assertIn("City." + town_city.id, objs)
        self.assertIn("Amenity." + AMENITY.id, objs)
        self.assertIn("Review." + REVIEW.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
