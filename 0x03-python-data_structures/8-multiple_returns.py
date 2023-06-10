#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence):
        new_tuple = len(sentence), sentence[0]
    else:
        new_tuple = len(sentence),
    return new_tuple
