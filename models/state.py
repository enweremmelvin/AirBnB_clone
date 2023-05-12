#!/usr/bin/env python3

"""
    this module contains a class that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        state class that inherits from BaseModel

        :CLASS ATTRIBUTES:
        name: string - empty string
    """

    name = ""
