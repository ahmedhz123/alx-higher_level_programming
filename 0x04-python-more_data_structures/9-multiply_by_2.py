#!/usr/bin/python3
def multiply_by_2(my_dict):
    my_new_dict = my_dict.copy()
    for k in sorted(my_new_dict.keys()):
        my_new_dict[k] = my_new_dict[k] * 2
    return my_new_dict    
