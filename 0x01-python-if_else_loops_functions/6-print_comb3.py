#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if j is 9 and i is 8:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}, ".format(i, j), end="")
