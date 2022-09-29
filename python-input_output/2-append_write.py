#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """ *** *** """
    with open(filename, 'a', encoding='utf-8') as f:
        return(f.write(text))
