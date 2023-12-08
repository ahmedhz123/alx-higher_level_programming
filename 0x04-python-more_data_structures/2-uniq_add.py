#!/usr/bin.python3
def uniq_add(my_list=[]):
    sum_t = 0
    for i in range(0, len(my_list)):
        if i == my_list.index(my_list[i]):
            sum_t += my_list[i]
        else:
            pass
    return sum_t
