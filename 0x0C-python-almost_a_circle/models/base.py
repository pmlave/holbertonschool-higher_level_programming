#!/usr/bin/python3
"""Base for all other classes and methods"""

import json


class Base:
    """Base class beginning"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Serialize the data into JSON'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Wrties the Json string to a file'''
        list_dicts = []
        """
        All instances in list will be same type ex. a list of all square
        instances or a list of all rectangle instances. Only need to do
        the following command once.
        """
        filer = "{}.json".format(cls.__name__)
        if list_objs is not None:
            '''Could be many representations, need to iterate through all'''
            for objects in list_objs:
                list_dicts.append(cls.to_dictionary(objects))
        with open(filer, "w") as file_write:
            file_write.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the Json string representation'''
        empty = []
        if json_string is None or len(json_string) == 0:
            return empty
        return json.loads(json_string)
