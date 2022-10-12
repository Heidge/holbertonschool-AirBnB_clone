#!/usr/bin/python3
"""
    Module FileStorage class
"""
import json
from models import base_model
import os


class FileStorage():
    """Class that serializes instances to a JSON file and deserializes JSON
    file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self,obj):
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """ deserializes JSON to __objects if JSON file (__file_path) """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objects_dict = json.load(f)
                for key, value in objects_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
