#!/usr/bin/python3
"""defining function"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
