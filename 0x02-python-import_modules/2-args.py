#!/usr/bin/python3
if __name__ is __main__:
    from sys import argv
    print(len(argv) - 1)
    print(" argument", end="")
    if (len(argv) - 1) is not 1:
        print("s:")
    else:
        print(":")
        for x in range(1, len(argv)):
            print("{:d}: {:s}".format(x, argv[x]))
