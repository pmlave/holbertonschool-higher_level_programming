#!/usr/bin/python3
for i in range(1, 100):
    if i is not 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:d}".format(i))
