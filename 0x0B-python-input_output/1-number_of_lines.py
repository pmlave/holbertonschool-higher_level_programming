#!/usr/bin/python3
def number_of_lines(filename=""):
    count = 0
    with open(filename) as f:
        for lines in f:
            count += 1
    return count
