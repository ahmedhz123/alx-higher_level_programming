#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(0, len(sentence)):
        if i == 0:
            first_char = sentence[i]
        i = i + 1
    if sentence == None:
        first_char = None
        return i, first_char
    else:
        return i, first_char    
