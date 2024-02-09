#!/usr/bin/python3
"""Defines the FileStorage class."""


import json
from os import path


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances."""


    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects


    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)


    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    cls_name, obj_id = k.split('.')
                    cls = globals()[cls_name]
                    self.__objects[k] = cls(**v)
