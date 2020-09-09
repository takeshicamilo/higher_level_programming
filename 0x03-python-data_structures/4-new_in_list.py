#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list.copy(my_list)
    if idx < 0 and idx > len(new_list):
        return my_list
    for i in range(0, len(new_list)):
        if i == idx:
            new_list[i] = element
            return new_list
