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
