#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if j > i and i is not 8 and j is not 9:
            print("{:d}{:d}, ".format(i, j), end="")
        elif j is 9 and i is 8:
            print("{:d}{:d}".format(i, j))
