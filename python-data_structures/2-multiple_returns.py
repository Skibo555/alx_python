#!/usr/bin/python3

def multiple_returns(sentence):
    i = len(sentence)
    j = sentence[0]
    if i == 0:
        return None
    else:
        return i, j