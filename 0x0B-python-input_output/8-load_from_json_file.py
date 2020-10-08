#!/usr/bin/python3
""" load from json file """
import json


def load_from_json_file(filename):
    """ load_from_json_file function """
    with open(filename) as file:
        json_file = json.load(file)
    return json_file
