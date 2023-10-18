#!/usr/bin/env python3
"""defination of the class FileStorage"""

from models.base_model import BaseModel
from models.user import User
import datetime
import json
import os


class FileStorage:
    
    """class for storing and retrieving information """
    __file_path = "file.join"
    __objects = {}
     
    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
            
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj
    
    #dump to json from file - serialize
    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        ser_dict = {}
        for key, obj in self.__objects.items():
            ser_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(ser_dict, file)

    #load from json to file - deserialize
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r")as FILE:
                data = json.load(FILE)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                if class_name == 'Place':
                    from models.place import Place
                    obj = Place(**value)
                elif class_name == 'State':
                    from models.state import State
                    obj = State(**value)
                elif class_name == 'City':
                    from models.city import City
                    obj = City(**value)
                elif class_name == 'Amenity':
                    from models.amenity import Amenity
                    obj = Amenity(**value)
                elif class_name == 'Review':
                    from models.review import Review
                    obj = Review(**value)
                else:
                    continue
                FileStorage.__objects[key] = obj
    except FileNotFoundError:
        pass
