#!/usr/bin/python3
"""defining function"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, 'w') as f:
        return f.write(json.dump(my_obj))
