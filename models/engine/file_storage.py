#!/usr/bin/python3
""" module for filestorage class """

import datetime
import json
import os


class FileStorage:
    """class for storing and retrieving data by json """
    __file_path = "file.json"
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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)
            
    def reload(self):
        """
        deserializes the JSON file to __objects only if the json file exists"""

        if not os.path.exists(FileStorage.__file_path):
            return

        try:
            deserialized = {}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                deserialized = json.load(f)
                
                 for key, value in deserialized.items():
                    cls_name = obj["__class__"]
                    if cls_name == 'BaseModel':
                        FileStorage.__objects[key] = obj

        except(FileNotFoundError, JSONDecodeError)
            pass
