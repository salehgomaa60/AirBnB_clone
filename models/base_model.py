#!/usr/bin/python3

"""This file defines  the BaseModel class which will
serve as the base of ou model."""

from uuid import uuid4
from datetime import datetime
import models import storage


class BaseModel:
    """ base class """

    def __init__(self, *args, **kwargs):
        """ serialize and deserialize class """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
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
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the class """
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp
