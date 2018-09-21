#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.keys())
    for i in range(len(a_dictionary)):
        print("{}: {}".format(a[i], a_dictionary[a[i]]))
