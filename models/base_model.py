#!/usr/bin/env python3

"""
    This module contains the class <BaseModel> \
    which will act as the base class for other \
    classes in this program
"""

import uuid
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

                if (val == "created_at") or (val == "updated_at"):
                    # assign datetime.strptime to x <to limit line chars -PEP8>
                    x = datetime.strptime

                    self.__dict__[val] = x(kwargs[val], "%Y-%m-%d %H:%M:%S.%f")
                else:
                    self.__dict__[val] = kwargs[val]

            return

        self.id = str(uuid.uuid4())

        # convert datetime from iso format
        iso_format = datetime.fromisoformat

        self.created_at = iso_format(datetime.now().isoformat())
        self.updated_at = iso_format(datetime.now().isoformat())

    def __str__(self):
        """
            return string representation in format: \
            [<class name>] (<self.id>) <self.__dict__>
        """

        value = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return value

    def save(self):
        """
            update the public instance attribute: \
            updated_at with the current datetime
        """

        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
            returns a dictionary containing all \
            keys/values of __dict__ of the instance
        """

        dict_vals = self.__dict__
        dict_vals["__class__"] = self.__class__.__name__

        dict_vals["created_at"] = str(dict_vals["created_at"])
        dict_vals["updated_at"] = str(dict_vals["updated_at"])

        return dict_vals
