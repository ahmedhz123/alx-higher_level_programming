#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if idx < 0:
            return
        elif idx > len(my_list):
            return
        elif i == idx:
            return(my_list[i])
