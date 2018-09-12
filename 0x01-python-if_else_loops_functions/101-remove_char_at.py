#!/usr/bin/python3
def remove_char_at(str, n):
    word = ""
    for i in range(len(str)):
        if i is not n:
            word += str[i]
        if i is n:
            continue

    return word
