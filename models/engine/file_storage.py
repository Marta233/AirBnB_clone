#!/usr/bin/python3
"""
A module to work with file storage engine
"""
from genericpath import isfile
import importlib
import json
from operator import mod
import os
from importlib import import_module
from json import JSONDecoder, JSONEncoder

class FileStorage:
    """
    represents The file storage for all data sets.
    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """
        Initializer for a class file Storage
        """
        self.import_classes = {
            'BaseMode': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self):
        """
        Returns a string representation of all objects

        Returns:
            dict: The stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        stores a new object to the dictionary

        Args:
            obj(BaseModel): an object to be stored
        """
        obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """
        serializes an object to json file
        """
        with open(self.__file_path,mode='w')as file:
            json_objs = {}
            for key, value in self.__objects.items():
                json_objs[key] = value.to_dict()
            file.write(JSONEncoder().encode(json_objs))
    
    def reload(self):
        """
        deserialized a python object to a JSON strin(if exists)
        """
        if os.path.isfile(self.__file_path):
            file_lines = []
            with open(self.__file_path, mode='r') as file:
                file_lines = file.readlines()
            file_txt = ''.join(file_lines) if len(file_lines) > 0 else '{}'
            json_objs = JSONDecoder().decode(file_txt)
            base_model_objs = dict()
            classes = self.model_classes
            for key, value in json_objs.items():
                cls_name = value['__class__']
                if cls_name in classes.key():
                    base_model_objs[key] = classes[cls_name](**value)