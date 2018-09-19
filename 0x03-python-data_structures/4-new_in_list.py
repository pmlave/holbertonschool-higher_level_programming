#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(len(new_list)):
        if i is idx:
            new_list[i] = element
            return new_list
