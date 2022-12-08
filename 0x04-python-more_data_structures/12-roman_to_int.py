#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        roman_dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 100
                }
        int_value = 0
        previous = 2000

        for c in roman_string:
            if roman_dict[c] > previous:
                int_value += roman_dict[c] - (previous * 2)
            else:
                int_value += roman_dict[c]
            previous = roman_dict[c]
        return int_value
    return 0
