#!/usr/bin/python3
"""
    Module FileStorage class
"""


class FileStorage():
    """Class that serializes instances to a JSON file and deserializes JSON
    file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self,obj):

    def save(self):

    def reload(self):
