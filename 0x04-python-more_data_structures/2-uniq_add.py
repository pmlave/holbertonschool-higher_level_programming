#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for i in range(len(my_list)):
        if my_list[i] not in unique:
            unique.append(my_list[i])
    return sum(unique)
