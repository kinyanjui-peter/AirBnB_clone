#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    #this class manages the attribute of city objects

    state_id = ""
    name = ""
