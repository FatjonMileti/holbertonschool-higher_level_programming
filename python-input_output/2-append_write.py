#!/usr/bin/python3
''' *** *** '''


def append_file(filename="", text=""):
    ''' *** *** '''
    with open(filename, 'a', encoding='utf-8') as f:
        return(f.write(text))
