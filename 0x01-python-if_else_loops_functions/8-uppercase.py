#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if char in range(97, 123):
            char -= 32
        print("{}".format(chr(char)), end="")
    print("")
