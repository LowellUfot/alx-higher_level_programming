#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict(a_dictionary)
    for i, j in new_dict.items():
        if j == value:
            del a_dictionary[i]
    return a_dictionary
