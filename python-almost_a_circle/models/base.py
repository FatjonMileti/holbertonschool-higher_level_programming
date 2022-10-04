#!/usr/bin/python3
''' *** *** '''
import json


class Base:
    ''' *** *** '''
    _nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base._nb_objects += 1
            self.id = Base._nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' *** *** '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        ''' *** *** '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy
