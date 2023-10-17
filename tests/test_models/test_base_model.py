#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
         baseM = BaseModel()
         baseM = BaseModel()
        self.assertNotEqual( baseM.id,  baseM.id)

    def test_two_models_different_created_at(self):
         baseM = BaseModel()
        sleep(0.05)
         baseM = BaseModel()
        self.assertLess( baseM.created_at, baseM.created_at)

    def test_two_models_different_updated_at(self):
         baseM = BaseModel()
        sleep(0.05)
         baseM = BaseModel()
        self.assertLess( baseM.updated_at,  baseM.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
         baseM = BaseModel()
         baseM.id = "123456"
         baseM.created_at =  baseM.updated_at = dt
         baseMstr =  baseM.__str__()
        self.assertIn("[BaseModel] (123456)",  baseMstr)
        self.assertIn("'id': '123456'",  baseMstr)
        self.assertIn("'created_at': " + dt_repr,  baseMstr)
        self.assertIn("'updated_at': " + dt_repr,  baseMstr)

    def test_args_unused(self):
         baseM = BaseModel(None)
        self.assertNotIn(None,  baseM.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
         baseM = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual( baseM.id, "345")
        self.assertEqual( baseM.created_at, dt)
        self.assertEqual( baseM.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        baseM = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(baseM.id, "345")
        self.assertEqual(baseM.created_at, dt)
        self.assertEqual(baseM.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_one_save(self):
        baseM = BaseModel()
        sleep(0.05)
        first_updated_at = baseM.updated_at
        baseM.save()
        self.assertLess(first_updated_at, baseM.updated_at)

    def test_two_saves(self):
        baseM = BaseModel()
        sleep(0.05)
        first_updated_at = baseM.updated_at
        baseM.save()
        second_updated_at = baseM.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        baseM.save()
        self.assertLess(second_updated_at, baseM.updated_at)

    def test_save_with_arg(self):
        baseM = BaseModel()
        with self.assertRaises(TypeError):
            baseM.save(None)

    def test_save_updates_file(self):
        baseM = BaseModel()
        baseM.save()
        baseMid = "BaseModel." + baseM.id
        with open("file.json", "r") as f:
            self.assertIn(baseMid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        baseM = BaseModel()
        self.assertTrue(dict, type(baseM.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        baseM = BaseModel()
        self.assertIn("id", baseM.to_dict())
        self.assertIn("created_at", baseM.to_dict())
        self.assertIn("updated_at", baseM.to_dict())
        self.assertIn("__class__", baseM.to_dict())

    def test_to_dict_contains_added_attributes(self):
        baseM = BaseModel()
        baseM.name = "Holberton"
        baseM.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", baseM.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        baseM = BaseModel()
        baseM_dict = baseM.to_dict()
        self.assertEqual(str, type(baseM_dict["created_at"]))
        self.assertEqual(str, type(baseM_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        baseM= BaseModel()
        baseM.id = "123456"
        baseM.created_at = baseM.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        baseM = BaseModel()
        self.assertNotEqual(baseM.to_dict(), baseM.__dict__)

    def test_to_dict_with_arg(self):
        baseM = BaseModel()
        with self.assertRaises(TypeError):
            baseM.to_dict(None)


if __name__ == "__main__":
    unittest.main()
