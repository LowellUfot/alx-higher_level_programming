#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        new_dict = a_dictionary
        new_dict[key] = value
       # if key in a_dictionary == True:
       #    a_dictionary[key] = value
       #     nds
       # else:
       #     a_dictionary[key] = value
        return new_dict
