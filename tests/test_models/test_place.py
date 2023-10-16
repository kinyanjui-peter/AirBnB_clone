#!/usr/bin/python3
"""Test Place"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testplace(unittest.TestCase):
    def test_pep8_place(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        PLACE= Place()
        self.assertEqual(PLACE.__class__.__name__, "Place")

    def test_MORE(self):
        PLACE = Place()
        self.assertTrue(issubclass(PLACE.__class__, BaseModel))
