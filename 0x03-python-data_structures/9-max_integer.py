#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        x = my_list[0]
        for i in range(0, len(my_list)):
            if x < my_list[i]:
                x = my_list[i]
    return x
