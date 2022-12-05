#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        length = len(sentence)

    if length == 0:
        return(length, None)

    return(length, sentence[0])
