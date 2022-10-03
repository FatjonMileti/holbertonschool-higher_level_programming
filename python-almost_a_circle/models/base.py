#!/usr/bin/python3
''' *** *** '''


class Base:
    ''' *** *** '''
    _nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            Base._nb_objects += 1
            self.id = Base._nb_objects
        else:
            self.id = id
