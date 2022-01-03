#!/usr/bin/python3
"""Module to add all argument"""

from sys import argv
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file = "add_item.json"
json_list = []

if path.exists(file) is False:
    save_to_json_file([], "add_item.json")
json_list = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    json_list.append(argv[i])
save_to_json_file(json_list, file)
    
