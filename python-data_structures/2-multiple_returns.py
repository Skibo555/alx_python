#!/usr/bin/python3

def multiple_returns(sentence):
    i = len(sentence)
    j = sentence
    if i == "":
        j = ()
        return None
    else:
        return i, j[0]
