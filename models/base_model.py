#!/usr/bin/python3

"""
    This module contains the class <BaseModel> \
    which will act as the base class for other \
    classes in this program
"""

import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
        This class defines all common \
        attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
            magic initialization method

            self.id => unique id for each instance \
            + the base model class

            self.created_at => current datetime when an instance is created

            self.updated_at => current datetime when an instance is created \
            + and it will be updated every time you change your object
        """

        # check is kwargs is not empty and create an instance \
        # with attributes and values from the kwargs dictionary passed in

        if kwargs:
            key_list = list(kwargs)

            for val in key_list:
                if val == ("__class__"):
                    continue

                # check if value of <created_at> and <updated_at> \
                # dictionary keys hold string values and convert to datetime \
                # objects if so; otherwise -> initialize value as is
                if (val == "created_at") or (val == "updated_at"):
                    if type(kwargs[val]) == str:
                        # initialize x to datetime.strptime \
                        # -> to comply witih PEP8 max line characters
                        x = datetime.strptime
                        kwargs[val] = x(kwargs[val], "%Y-%m-%dT%H:%M:%S.%f")

                self.__dict__[val] = kwargs[val]

            return

        self.id = str(uuid.uuid4())

        # initialize created_at and updated_at public instance variables
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # if its a new instance that is being initialized (not from kwargs) \
        # add a call to the method new(self) on storage
        storage.new(self)

    def __str__(self):
        """
            return string representation in format: \
            [<class name>] (<self.id>) <self.__dict__>
        """

        # create temp dictionary and delete the __class__ key \
        # value pair from the temp dict
        temp_dict = {}

        for key, value in self.__dict__.items():
            if key == "__class__":
                continue

            temp_dict[key] = value

        value = f"[{self.__class__.__name__}] ({self.id}) {temp_dict}"
        return value

    def save(self):
        """
            update the public instance attribute: \
            updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all \
            keys/values of __dict__ of the instance
        """

        # temporary dict to hold dict_vals <seld.__dict__> values \
        # this dictionary is created so <created_at> and \
        # <updated_at> values get converted to str without being \
        # changed to str in the class itself
        temp_dict = {}

        dict_vals = self.__dict__
        dict_vals["__class__"] = self.__class__.__name__

        # convert <created_at> and <updated_at> time values to str \
        # and assign to temp_dict
        for key, val in dict_vals.items():
            if (key == "created_at") or (key == "updated_at"):
                # check if <created_at> or <updated_at> is a string \
                # if true -> add to dict \
                # otherwise -> convert to isoformat() of datetime
                # this condition is being implemented to correctly return a \
                # dictionary of an instance whose values are the to_dict() \
                # return value of another instance; here the datetime \
                # attributes <created_at> and <updated_at> will be strings
                if type(val) is not str:
                    temp_dict[key] = val.isoformat()
                else:
                    temp_dict[key] = val
            else:
                temp_dict[key] = val

        return temp_dict
