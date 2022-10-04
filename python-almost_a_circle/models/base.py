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

    @classmethod
    def load_from_file(cls):
        ''' *** *** '''
        filename = cls.__name__ + ".json"
        if path.exists(filename) is False:
            return []

        with open(filename, "r", encoding="utf-8") as f:
            objs = cls.from_json_string(f.read())
            instances = [cls.create(**elem) for elem in objs]
            return instances
