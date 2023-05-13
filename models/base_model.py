#!/usr/bin/env python3

"""
    This module contains the class <BaseModel> \
    which will act as the base class for other \
    classes in this program
"""

import uuid
from models import storage
from datetime import datetime


class BaseModel():
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
                if val == "__class__":
                    continue

                self.__dict__[val] = kwargs[val]

            return

        self.id = str(uuid.uuid4())

        # initialize created_at and updated_at public instance variables
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

        # if its a new instance that is being initialized (not from kwargs) \
        # add a call to the method new(self) on storage
        storage.new(self)

    def __str__(self):
        """
            return string representation in format: \
            [<class name>] (<self.id>) <self.__dict__>
        """

        if (type(self.created_at) is str) and (type(self.updated_at) is str):
            x = datetime.strptime

            self.created_at = x(str(self.created_at), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = x(str(self.updated_at), "%Y-%m-%dT%H:%M:%S.%f")

        value = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return value

    def save(self):
        """
            update the public instance attribute: \
            updated_at with the current datetime
        """

        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all \
            keys/values of __dict__ of the instance
        """

        dict_vals = self.__dict__
        dict_vals["__class__"] = self.__class__.__name__

        # convert datetime (created_at and updated_at) public instance fields \
        # to datetime iso format
        to_iso = datetime.isoformat

        if type(dict_vals["created_at"]) is not str:
            dict_vals["created_at"] = to_iso(dict_vals["created_at"])
        if type(dict_vals["updated_at"]) is not str:
            dict_vals["updated_at"] = to_iso(dict_vals["updated_at"])

        return dict_vals
