#!/usr/bin/env python3
"""
defination of the class model
"""
import uuid
from datetime import datetime
from engine import file_storage

class BaseModel:
    """initinize the attribute
    arge:
        args: receives variable non-keyworded argumenuts
        kwargs: receives keyworded arguments

    Constructor method(__init__) called when creating an object
        """
    def __init__(self, *args, **kwargs):
        #check if kwargs is empty  
        if kwargs:
            #loop through the kwargs items
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                #check keys match, attribute is updated with datetime value
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    #if keys dont match the above, attribute are set with passed values
                    setattr(self, key, value)
        #if no kwargs provided. i.e for args
        else:
            #generate uuid4 and update update_at and created_at to current time
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        # Check if it's a new instance (not from a dictionary representation)
        if not args and not kwargs:
            storage.new(self)

    #set a string representation for __str__
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"

    #updates updated_at with current time
    def save(self):
        self.updated_at = datetime.now()

    #access the attribute and update the time to iso standard
    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        dict_obj["__class__"] = self.__class__.__name__
        return dict_obj

