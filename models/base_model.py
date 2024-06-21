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
          
        """
         DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
         self.id = str(uuid4())
         self.created_at = datetime.utcnow()
         self.updated_at = datetime.utcnow()
         
    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates updated variable"""
        self.updated_at = datetime.utcnow()
        
    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
