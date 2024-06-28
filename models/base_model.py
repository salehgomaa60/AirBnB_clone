#!/usr/bin/python3

"""This file defines  the BaseModel class which will
serve as the base of ou model."""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base class"""

    def __init__(self):
        """Initialize instance attributes."""
        
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
        """Convert instance attributes to dictionary."""
        
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
    
