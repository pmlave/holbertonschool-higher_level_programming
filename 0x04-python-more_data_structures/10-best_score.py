#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and a_dictionary != {}:
        a = sorted(a_dictionary.keys())
        highest = 0
        for i in range(len(a_dictionary)):
            test = a_dictionary[a[i]]
            if test > highest:
                highest = test
                high_key = a[i]
        return high_key
    else:
        return None
