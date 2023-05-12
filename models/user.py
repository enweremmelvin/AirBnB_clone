#!/usr/bin/env python3

"""
    this module contains a user \
    class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        user class that inherits from BaseModel
    """

    email = ""
    password = ""
    last_name = ""
    first_name = ""
