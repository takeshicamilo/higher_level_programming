#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for z in range(x):
            print(my_list[z], end="")
            length += 1
    except:
        pass
    print()
    return length
