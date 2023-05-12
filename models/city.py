#!/usr/bin/env python3

"""
    this module contains a class \
    <City> that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        <City> class inherits from BaseModel

        :CLASS ATTRIBUTES:
        name: string - empty string
        state_id: string - empty string: it will be the State.id
    """

    name = ""
    state_id = ""
