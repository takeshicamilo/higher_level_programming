#!/usr/bin/python3
def uppercase(str):
    asc = list(str)
    for i in range(len(asc)):
        if (ord(asc[i]) > 96 and ord(asc[i]) < 123):
            asc[i] = chr(ord(asc[i]) - 32)
    print("{}".format(("").join(asc)))
