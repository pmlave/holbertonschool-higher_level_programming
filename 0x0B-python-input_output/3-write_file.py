#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w+') as f:
        q = f.write(text)
        return q
