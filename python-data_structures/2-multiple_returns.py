#!/usr/bin/python3

def multiple_returns(sentence):
    i = len(sentence)
    j = sentence[0]
    if sentence[0] == "":
        return None
    return i, j