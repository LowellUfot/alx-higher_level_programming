#!/usr/bin/python3
def to_upper(char):
    if ord(char) >= 97 and ord(char) < 123:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(str):
    new = ""
    for char in str:
        new += "%c" % to_upper(char)
    print("{:s}".format(new))
