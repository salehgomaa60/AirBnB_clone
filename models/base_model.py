#!/usr/bin/python3

"""This file defines  the BaseModel class which will
serve as the base of ou model."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ base class """

    def __init__(self, *args, **kwargs):
        """ serialize and deserialize class """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        """deserialize of kwargs"""
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for key, val in kwargs.items():
            if key == "__class__":
                continue
            setattr(self, key, val)
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """overide str representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
            type(self).__name__,
            self.id,
            self.__dict__)

    def save(self):
        """updating instance variable updated at """
        self.updated_at = datetime.utcnow()
        models.storage.save()
        

    def to_dict(self):
        """Convert instance attributes to dictionary."""
        
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
    
