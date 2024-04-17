#!/usr/bin/python3
"""defining function"""


import json


def save_to_json_file(my_obj, filename, encoding='utf-8'):
    """function that writes an Object to a text file"""
    with open (filename, 'w') as f:
        json.dump(my_obj, filename, ensure_ascii=False, indent=4)
