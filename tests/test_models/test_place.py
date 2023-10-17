#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(PLACE))
        self.assertNotIn("user_id", PLACE.__dict__)

    def test_name_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(PLACE))
        self.assertNotIn("name", PLACE.__dict__)

    def test_description_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(PLACE))
        self.assertNotIn("desctiption", PLACE.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(PLACE))
        self.assertNotIn("number_rooms", PLACE.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(PLACE))
        self.assertNotIn("number_bathrooms", PLACE.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(PLACE))
        self.assertNotIn("max_guest", PLACE.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        PLACE= Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(PLACE))
        self.assertNotIn("price_by_night", PLACE.__dict__)

    def test_latitude_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(PLACE))
        self.assertNotIn("latitude", PLACE.__dict__)

    def test_longitude_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(PLACE))
        self.assertNotIn("longitude", PLACE.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        PLACE = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(PLACE))
        self.assertNotIn("amenity_ids", PLACE.__dict__)

    def test_two_places_unique_ids(self):
        PLACE1 = Place()
        PLACE2 = Place()
        self.assertNotEqual(PLACE1.id, PLACE2.id)

    def test_two_places_different_created_at(self):
        PLACE1 = Place()
        sleep(0.05)
        PLACE2 = Place()
        self.assertLess(PLACE1.created_at, PLACE2.created_at)

    def test_two_places_different_updated_at(self):
        PLACE1 = Place()
        sleep(0.05)
        PLACE2 = Place()
        self.assertLess(PLACE1.updated_at, PLACE2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        PLACE = Place()
        PLACE.id = "123456"
        PLACE.created_at = PLACE.updated_at = dt
        plstr = PLACE.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        PLACE = Place(None)
        self.assertNotIn(None, PLACE.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        PLACE= Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(PLACE.id, "345")
        self.assertEqual(PLACE.created_at, dt)
        self.assertEqual(PLACE.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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
        PLACE = Place()
        sleep(0.05)
        first_updated_at = PLACE.updated_at
        PLACE.save()
        self.assertLess(first_updated_at, PLACE.updated_at)

    def test_two_saves(self):
        PLACE = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        PLACE.save()
        second_updated_at = PLACE.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        PLACE.save()
        self.assertLess(second_updated_at, PLACE.updated_at)

    def test_save_with_arg(self):
        PLACE = Place()
        with self.assertRaises(TypeError):
            PLACE.save(None)

    def test_save_updates_file(self):
        PLACE = Place()
        PLACE.save()
        PLACEid = "Place." + PLACE.id
        with open("file.json", "r") as f:
            self.assertIn(PLACEid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        PLACE = Place()
        self.assertIn("id", PLACE.to_dict())
        self.assertIn("created_at", PLACE.to_dict())
        self.assertIn("updated_at", PLACE.to_dict())
        self.assertIn("__class__", PLACE.to_dict())

    def test_to_dict_contains_added_attributes(self):
        PLACE = Place()
        PLACE.middle_name = "Holberton"
        PLACE.my_number = 98
        self.assertEqual("Holberton", PLACE.middle_name)
        self.assertIn("my_number", PLACE.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        PLACE = Place()
        pl_dict = PLACE.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        PLACE= Place()
        PLACE.id = "123456"
        PLACE.created_at = PLACE.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(PLACE.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        PLACE = Place()
        self.assertNotEqual(PLACE.to_dict(), PLACE.__dict__)

    def test_to_dict_with_arg(self):
        PLACE = Place()
        with self.assertRaises(TypeError):
            PLACE.to_dict(None)


if __name__ == "__main__":
    unittest.main()
