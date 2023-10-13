#!/usr/bin/python3
''' this module creates a  review class'''

from models.BaseModel import BaseModel

class reviews(BaseModel):

    '''the class to manage objects attribute for the review '''
     
    place_id = ""
    user_id = ""
    text = ""
