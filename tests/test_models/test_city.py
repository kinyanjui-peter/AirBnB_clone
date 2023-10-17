#!/usr/bin/python3
"""Defines unittests for models/city.py.

"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        town_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(town_city))
        self.assertNotIn("state_id", town_city.__dict__)

    def test_name_is_public_class_attribute(self):
        town_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(town_city))
        self.assertNotIn("name", town_city.__dict__)

    def test_two_cities_unique_ids(self):
        town_city1 = City()
        town_city2 = City()
        self.assertNotEqual(town_city1.id, town_city2.id)

    def test_two_cities_different_created_at(self):
        town_city1 = City()
        sleep(0.05)
        town_city2 = City()
        self.assertLess(town_city1.created_at, town_city2.created_at)

    def test_two_cities_different_updated_at(self):
        town_city1 = City()
        sleep(0.05)
        town_city2 = City()
        self.assertLess(town_city1.updated_at, town_city2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        town_city = City()
        town_city.id = "123456"
        town_city.created_at = town_city.updated_at = dt
        cystr = town_city.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        town_city = City(None)
        self.assertNotIn(None, town_city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        town_city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(town_city.id, "345")
        self.assertEqual(town_city.created_at, dt)
        self.assertEqual(town_city.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

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
        town_city = City()
        sleep(0.05)
        first_updated_at = town_city.updated_at
        town_city.save()
        self.assertLess(first_updated_at, town_city.updated_at)

    def test_two_saves(self):
        town_city = City()
        sleep(0.05)
        first_updated_at = town_city.updated_at
        town_city.save()
        second_updated_at = town_city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        town_city.save()
        self.assertLess(second_updated_at, town_city.updated_at)

    def test_save_with_arg(self):
        town_city = City()
        with self.assertRaises(TypeError):
            town_city.save(None)

    def test_save_updates_file(self):
        town_city = City()
        town_city.save()
        town_cityid = "City." + town_city.id
        with open("file.json", "r") as f:
            self.assertIn(town_cityid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        town_city= City()
        self.assertIn("id", town_city.to_dict())
        self.assertIn("created_at", town_city.to_dict())
        self.assertIn("updated_at", town_city.to_dict())
        self.assertIn("__class__", town_city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        town_city = City()
        town_city.middle_name = "Holberton"
        town_city.my_number = 98
        self.assertEqual("Holberton", town_city.middle_name)
        self.assertIn("my_number", town_city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        town_city = City()
        town_city_dict = town_city.to_dict()
        self.assertEqual(str, type(town_city_dict["id"]))
        self.assertEqual(str, type(town_city_dict["created_at"]))
        self.assertEqual(str, type(town_city_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        town_city = City()
        town_city.id = "123456"
        town_city.created_at = town_city.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(town_city.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        town_city = City()
        self.assertNotEqual(town_city.to_dict(), town_city.__dict__)

    def test_to_dict_with_arg(self):
        town_city = City()
        with self.assertRaises(TypeError):
            town_city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
