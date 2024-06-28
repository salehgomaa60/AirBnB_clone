#!/usr/bin/python3

"""This file defines  the BaseModel class which will
serve as the base of ou model."""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """base class """
    def __init__(self):
        """ constructor initializing the base class"""
        self.id = str(uuid4())
         self.created_at = datetime.utcnow()
         self.updated_at = datetime.utcnow()

    def __str__(self):
        """ str representation of object """
        fmt = "[{}] ({}) {}"
        return fmt.format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """updating instance variable updated at """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary representation of the class """
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp
    
