#!/usr/bin/python3
"""Base module for airbnb clone"""
import cmd, sys, uuid
from datetime import datetime

class BaseModel:
    """Base class for airbnb clone"""


    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        dictionary_str = self.__dict__.copy()
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat
        dictionary["updated_at"] = self.updated_at.isoformat
        return (self.__dict__)

