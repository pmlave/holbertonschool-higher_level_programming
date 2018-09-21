#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = ()
    new_set = set_1 - set_2
    new_set.update(set_2 - set_1)
    return new_set
