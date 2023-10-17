#!/usr/bin/python3
"""Defines unittests for models/review.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        REVIEW = Review()
        sleep(0.05)
        REVIEW2 = Review()
        self.assertLess(REVIEW.updated_at, REVIEW2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        REVIEW = Review()
        REVIEW.id = "123456"
        REVIEW.created_at = REVIEW.updated_at = dt
        REVIEWstr = REVIEW.__str__()
        self.assertIn("[Review] (123456)", REVIEWstr)
        self.assertIn("'id': '123456'", REVIEWstr)
        self.assertIn("'created_at': " + dt_repr, REVIEWstr)
        self.assertIn("'updated_at': " + dt_repr, REVIEWstr)

    def test_args_unused(self):
        REVIEW = Review(None)
        self.assertNotIn(None, REVIEW.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        REVIEW = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(REVIEW.id, "345")
        self.assertEqual(REVIEW.created_at, dt)
        self.assertEqual(REVIEW.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        REVIEW = Review()
        sleep(0.05)
        first_updated_at = REVIEW.updated_at
        REVIEW.save()
        self.assertLess(first_updated_at, REVIEW.updated_at)

    def test_two_saves(self):
        REVIEW = Review()
        sleep(0.05)
        first_updated_at = REVIEW.updated_at
        REVIEW.save()
        second_updated_at = REVIEW.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        REVIEW.save()
        self.assertLess(second_updated_at, REVIEW.updated_at)

    def test_save_with_arg(self):
        REVIEW = Review()
        with self.assertRaises(TypeError):
            REVIEW.save(None)

    def test_save_updates_file(self):
        REVIEW = Review()
        REVIEW.save()
        REVIEWid = "Review." + REVIEW.id
        with open("file.json", "r") as f:
            self.assertIn(REVIEWid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        REVIEW = Review()
        self.assertIn("id", REVIEW.to_dict())
        self.assertIn("created_at", REVIEW.to_dict())
        self.assertIn("updated_at", REVIEW.to_dict())
        self.assertIn("__class__", REVIEW.to_dict())

    def test_to_dict_contains_added_attributes(self):
        REVIEW = Review()
        REVIEW.middle_name = "Holberton"
        REVIEW.my_number = 98
        self.assertEqual("Holberton", REVIEW.middle_name)
        self.assertIn("my_number", REVIEW.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        REVIEW = Review()
        REVIEW_dict = REVIEW.to_dict()
        self.assertEqual(str, type(REVIEW_dict["id"]))
        self.assertEqual(str, type(REVIEW_dict["created_at"]))
        self.assertEqual(str, type(REVIEW_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        REVIEW = Review()
        REVIEW.id = "123456"
        REVIEW.created_at = REVIEW.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(REVIEW.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        REVIEW = Review()
        self.assertNotEqual(REVIEW.to_dict(), REVIEW.__dict__)

    def test_to_dict_with_arg(self):
        REVIEW = Review()
        with self.assertRaises(TypeError):
            REVIEW.to_dict(None)


if __name__ == "__main__":
    unittest.main()
