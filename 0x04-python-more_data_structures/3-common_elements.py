#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for i in list(set_1):
        for j in list(set_2):
            if i == j:
                my_list = j
            else:
                pass
    return my_list        
