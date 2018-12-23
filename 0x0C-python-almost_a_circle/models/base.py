#!/usr/bin/python3
"""Base for all other classes and methods"""

import json

class Base:
    """Base class beginning"""
    __nb_objects = 0
    __file_path = "file.json"

    def __init__(self, id=None):
        """Class constructor for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''Serialize the data into JSON'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            for each_dict in list_dictionaries:
                return json.dumps(each_dict)
