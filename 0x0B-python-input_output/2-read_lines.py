#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    count = 1
    with open(filename) as f:
        for lines in f:
            if count <= nb_lines or nb_lines <= 0:
                print(lines, end='')
            count += 1
