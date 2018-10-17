#!/usr/bin/python3
import sys
import pathlib
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    new_object = load_from_json_file(filename)
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        new_object.append(sys.argv[i])
    save_to_json_file(new_object, filename)
except FileNotFoundError:
    new_object = []
    with open(filename, 'a+') as f:
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            new_object.append(sys.argv[i])
        save_to_json_file(new_object, filename)
