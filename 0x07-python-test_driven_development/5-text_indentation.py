#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    for remove in ".:?":
        text = (remove + "\n\n").join(
            [line.strip(" ") for line in text.split(remove)])

    print("{}".format(text), end="")
