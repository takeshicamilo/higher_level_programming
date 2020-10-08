#!/usr/bin/python3
""" 7 save to json file """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json file function """

    with open(filename, "w", encoding="utf-8") as file:
        jsonfile = json.dumps(my_obj)
        file.write(jsonfile)
