#!/usr/bin/env python3
"""defination of the class FileStorage"""

#from base_model import BaseModel
import file_storage
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
        return self._objects
            
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
        for key, obj in self.objects.items():
            ser_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(ser_dict, file)

    #load from json to file - deserialize
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        #try:
        #    with open(self.__file_path, "r") as file:
        #        ser_obj = json.load(file)
        #    for key, value in ser_dict.items():
        #        class_name, obj_id = key.split(".")
        #        self.__objcts[key] = globls()[class_name](**value)
        if os.path.isfile(Filestorage.__file_path):
            with open(Filestorage.__file_path, "r")as FILE:
                for key, value in dictionary.items():
                    obj = eval(value['__class__'])(**value)
                    obj = FileStorage.__objects[key]
