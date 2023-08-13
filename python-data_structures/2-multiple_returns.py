#!/usr/bin/python3

def multiple_returns(sentence):
    i = len(sentence)
    j = sentence[0]
    if j is "":
        return None
    return i, j