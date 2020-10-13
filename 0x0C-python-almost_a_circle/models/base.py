#!/usr/bin/python3
""" base.py """
import json
import os


class Base():
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string method """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file method  """

        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is None:
            new_list = []
        else:
            for i in list_objs:
                new_list.append(i.to_dictionary())
        json_file = Base.to_json_string(new_list)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_file)

    @staticmethod
    def from_json_string(json_string):
        """ from json string method """

        new_list = []
        if json_string is None:
            return new_list
        new_list = json_string
        obj = json.loads(new_list)
        return obj

    @classmethod
    def create(cls, **dictionary):
        """ create method """

        class_name = cls.__name__
        if class_name == "Rectangle":
            new = cls(1, 1)
        elif class_name == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ load from file method """

        filename = cls.__name__ + ".json"
        new_list = []

        if os.path.isfile(filename):
            with open(filename) as file:
                new_dict = cls.from_json_string(file.read())
                for x in new_dict:
                    new_list.append(cls.create(**x))
                return new_list

        else:
            return []
