#!/usr/bin/python3
"""Defines the FileStorage class."""


import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances.
    Class Methods:
        all: Returns the object
        new: updates the dictionary id
        save: Serializes, or converts Python objects into JSON strings
        reload: Deserializes, or converts JSON strings into Python objects.
    Class Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        class_dict (dict): A dictionary of all the classes.
    """


    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}


    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects


    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    cls_name, obj_id = k.split('.')
                    cls = globals()[cls_name]
                    self.__objects[k] = cls(**v)
