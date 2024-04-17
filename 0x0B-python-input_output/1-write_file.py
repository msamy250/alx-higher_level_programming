#!/usr/bin/python3
"""defining function"""


def write_file(filename="", text=""):
    """function that write a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
