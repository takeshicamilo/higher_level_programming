#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list and not idx:
        return my_list
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                del my_list[i]
        return my_list
