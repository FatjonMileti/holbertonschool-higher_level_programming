#!/usr/bin/python3
''' *** *** '''
from os import path
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    j_file = load_from_json_file('add_item.json')
else:
    j_file = []

for i in range(1, len(argv)):
    j_file.append(argv[i])

save_to_json_file(j_file, 'add_item.json')
