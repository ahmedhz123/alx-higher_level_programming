#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary.keys():
        if i == key:
            a_dictionary[i] = value
    if key != i:       
        a_dictionary[key] = value
    return a_dictionary        
