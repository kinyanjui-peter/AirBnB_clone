#!/usr/bin/python3
"""File Storage Class"""


import json
from models.base_model import BaseModel as Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    This class implements a file storage module for serializing instances
    to a JSON file and deserializing JSON files to instances.
    """

    __file_path = "file.json"  # Path for the JSON file
    __objects = {}  # Dictionary to store objects

    def all(self):
        """
        Retrieves the dictionary containing all objects.

        Returns:
            dict: A dictionary containing all objects.
        """
        return self.__objects

    def new(self, instance):
        """
        Adds a new instance to the dictionary of objects.

        Args:
            instance: The instance to be added.
        """
        class_name = instance.__class__.__name__
        self.__objects[f"{class_name}.{instance.id}"] = instance

    def save(self):
        """
        Serializes the objects dictionary to a JSON file.
        The path to the JSON file is specified by __file_path.
        """
        object_dictionary = {}
        for key, instance in self.__objects.items():
            object_dictionary[key] = instance.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(object_dictionary, file)

    def reload(self):
        """
        Deserializes the JSON file and updates the objects dictionary.
        If the JSON file (__file_path) exists, it reads the file
        and loads the objects. If the file doesn't exist, it does nothing.
        """
        class_list = {
            'BaseModel': Base,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
            'User': User
        }

        try:
            with open(self.__file_path, "r") as file:
                object_dictionary = json.load(file)
                for key, value in object_dictionary.items():
                    class_name, instance_id = key.split(".")
                    self.__objects[key] = class_list[class_name](**value)
        except FileNotFoundError:
            pass
