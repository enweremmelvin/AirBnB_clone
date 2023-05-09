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

    def __init__(self):
        """
            magic initialization method

            self.id => unique id for each instance \
            + the base model class

            self.created_at => current datetime when an instance is created
            self.updated_at => current datetime when an instance is created \
            + and it will be updated every time you change your object
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

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

        return dict_vals
