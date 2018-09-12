#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
            print("{}".format(chr(ord(str[i]) - 32)) if 96 < ord(str[i]) < 123
                  else str[i], end="")
    print()
