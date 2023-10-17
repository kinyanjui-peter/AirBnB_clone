#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        AMENITY = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        AMENITY = Amenity()
        AMENITY1 = Amenity()
        self.assertNotEqual(AMENITY.id, AMENITY1.id)

    def test_two_amenities_different_created_at(self):
        AMENITY = Amenity()
        sleep(0.05)
        AMENITY1 = Amenity()
        self.assertLess(AMENITY.created_at, AMENITY1.created_at)

    def test_two_amenities_different_updated_at(self):
        AMENITY = Amenity()
        sleep(0.05)
        AMENITY1 = Amenity()
        self.assertLess(AMENITY.updated_at, AMENITY1.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        AMENITY = Amenity()
        AMENITY.id = "123456"
        AMENITY.created_at = AMENITY.updated_at = dt
        AMENITYstr = AMENITY.__str__()
        self.assertIn("[Amenity] (123456)", AMENITYstr)
        self.assertIn("'id': '123456'", AMENITYstr)
        self.assertIn("'created_at': " + dt_repr, AMENITYstr)
        self.assertIn("'updated_at': " + dt_repr, AMENITYstr)

    def test_args_unused(self):
        AMENITY = Amenity(None)
        self.assertNotIn(None, AMENITY.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        AMENITY = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(AMENITY.id, "345")
        self.assertEqual(AMENITY.created_at, dt)
        self.assertEqual(AMENITY.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

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
        AMENITY = Amenity()
        sleep(0.05)
        first_updated_at = AMENITY.updated_at
        AMENITY.save()
        self.assertLess(first_updated_at, AMENITY.updated_at)

    def test_two_saves(self):
        AMENITY = Amenity()
        sleep(0.05)
        first_updated_at = AMENITY.updated_at
        AMENITY.save()
        second_updated_at = AMENITY.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        AMENITY.save()
        self.assertLess(second_updated_at, AMENITY.updated_at)

    def test_save_with_arg(self):
        AMENITY = Amenity()
        with self.assertRaises(TypeError):
            AMENITY.save(None)

    def test_save_updates_file(self):
        AMENITY = Amenity()
        AMENITY.save()
        AMENITYid = "Amenity." + AMENITY.id
        with open("file.json", "r") as f:
            self.assertIn(AMENITYid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        AMENITY = Amenity()
        self.assertIn("id", AMENITY.to_dict())
        self.assertIn("created_at", AMENITY.to_dict())
        self.assertIn("updated_at", AMENITY.to_dict())
        self.assertIn("__class__", AMENITY.to_dict())

    def test_to_dict_contains_added_attributes(self):
        AMENITY = Amenity()
        AMENITY.middle_name = "Holberton"
        AMENITY.my_number = 98
        self.assertEqual("Holberton", AMENITY.middle_name)
        self.assertIn("my_number", AMENITY.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        AMENITY = Amenity()
        AMENITY_dict = AMENITY.to_dict()
        self.assertEqual(str, type(AMENITY_dict["id"]))
        self.assertEqual(str, type(AMENITY_dict["created_at"]))
        self.assertEqual(str, type(AMENITY_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        AMENITY = Amenity()
        AMENITY.id = "123456"
        AMENITY.created_at = AMENITY.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(AMENITY.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        AMENITY = Amenity()
        self.assertNotEqual(AMENITY.to_dict(), AMENITY.__dict__)

    def test_to_dict_with_arg(self):
        AMENITY = Amenity()
        with self.assertRaises(TypeError):
            AMENITY.to_dict(None)


if __name__ == "__main__":
    unittest.main()

