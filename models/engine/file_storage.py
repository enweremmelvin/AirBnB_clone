#!/usr/bin/env python3

"""
    This module contains a class <FileStorage> that \
    serializes/de-serializes a JSON file
"""

import os
import json
from datetime import datetime


class FileStorage():
    """
        This class serializes instances to a JSON file \
        and deserializes JSON file to instances
    """

    __objects = dict()
    __file_path = "objects.json"

    def all(self):
        """
            return the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """

        dict_val = obj
        dict_key = obj.__class__.__name__ + "." + obj.id

        self.__objects[dict_key] = dict_val

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """

        json_obj = {}
        obj_key_list = list(self.__objects)

        # create a list of the dictionary representation of all objects \
        # stored in the self.__objects private class field
        for val in obj_key_list:
            json_obj[f"{val}"] = self.__objects[val].to_dict()

        # dump list of dictionary representation to json
        json_obj = json.dumps(json_obj)

        with open(self.__file_path, mode="w", encoding="utf-8") as file_handle:
            file_handle.write(json_obj)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file \
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t \
            exist, no exception should be raised)
        """

        # import needed classes from their modules in the models package \
        # this import is placed here to prevent circular import errors
        from models.user import User
        from models.base_model import BaseModel

        # check if file <self.__file_path> exists
        check_file = os.path.exists(self.__file_path)

        if not check_file:
            return

        # dictionary of classes -> key = class name -> value = \
        # memory representation of class
        class_dict = {"BaseModel": BaseModel, "User": User}

        with open(self.__file_path, mode="r", encoding="utf-8") as file_handle:
            json_obj = file_handle.read()
            json_obj = json.loads(json_obj)

            # import BaseModel and instantiate new instances with values \
            # from json file
            for key, val in json_obj.items():
                # find name of class to initialize an instance of \
                # and store key/value pairs in __objects dictionary
                class_name = None

                for cls_key, value in class_dict.items():
                    if key.startswith(cls_key):
                        class_name = value
                        break

                if class_name != None:
                    self.__objects[key] = class_name(**val)
