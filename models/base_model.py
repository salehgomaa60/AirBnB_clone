#!/usr/bin/python3
"""
this class is a base class for the project 
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates a dict representations.
        save(self): updates instance arttributes with current datetime.
        to_dict(self): returns the dictionary values of the instance object.

    """

    def __init__(self):
         """Public instance artributes initialization

        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values

        """
         DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
         self.id = str(uuid4())
         self.created_at = datetime.now()
         self.updated_at = datetime.now()
         
    def __str__(self):
        """
returns a string representation of the class 
"""
        return "[{}] ({}) {}".format(self.__class__.name, self.id, self.__dict__)

    def save(self):
        """
updates the public instance attribute updated at with the current date time 
"""
        
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method returns a dictionary containing all 
        keys/values of __dict__ instance
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
