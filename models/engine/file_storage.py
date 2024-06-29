#!/usr/bin/python3
""" module for filestorage class """

import datetime
import json
import os


class FileStorage:
    """class for storing and retrieving data by json """
    __file_path = ""
    __objects = {}

    def all(self):
        """ return the dictionary __objects"""
        return FileStorage.__objects

    def new (self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding = "utf-8") as f:
        for key, value in FileStorage.__objects.items():
            serialized = {key: value.to_dict()}
            
        json.dump(serialized, f)
        
    def reload(self):
        """
        deserializes the JSON file to __objects only if the json file exists"""

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return
            
