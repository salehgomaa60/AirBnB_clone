#!/usr/bin/python3

""" Update models/__init__.py: to create a unique FileStorage instances """

from models.engine.file_storage import FileStorage
""" getting the storage instance """
storage = FileStorage()
storage.reload()
