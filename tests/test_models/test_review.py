#!/usr/bin/python3
"""Test Review"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testreview(unittest.TestCase):
    def test_pep8_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        REVIEW = Review()
        self.assertEqual(REVIEW.__class__.__name__, "Review")

    def test_father(self):
        REVIEW = Review()
        self.assertTrue(issubclass(REVIEW.__class__, BaseModel))
