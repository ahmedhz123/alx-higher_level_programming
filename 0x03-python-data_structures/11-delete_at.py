#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                my_list.remove(idx + 1)
            else:
                pass
        return my_list        
