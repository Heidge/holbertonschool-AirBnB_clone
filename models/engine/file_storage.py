#!/usr/bin/python3
"""
    Module FileStorage class
"""
import json


class FileStorage():
    """Class that serializes instances to a JSON file and deserializes JSON
    file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self,obj):
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        dictionary = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)
