#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstLetter = sentence[0]

    if length == 0:
        return (length, None)

    tupleReturn = length, firstLetter
    return tupleReturn
