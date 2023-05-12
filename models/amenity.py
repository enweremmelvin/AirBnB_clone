#!/usr/bin/env python3

"""
    this module contains a class <Amenity> that \
    inherits from the BaseModel class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        <Amenity> class inheriting from the BaseModel class

        :CLASS ATTRIBUTES:
        name: string - empty string
    """

    name = ""
