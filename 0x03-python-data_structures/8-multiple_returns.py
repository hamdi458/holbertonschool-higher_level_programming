#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        x = None
    else:
        x = sentence[0]
    return len(sentence), x
