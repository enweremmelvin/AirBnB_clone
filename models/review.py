#!/usr/bin/env python3

"""
    this module contains a class: \
    <Review> that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        class inheriting from BaseModel

        text: string - empty string
        user_id: string - empty string: it will be the User.id
        place_id: string - empty string: it will be the Place.id
    """

    text = ""
    user_id = ""
    place_id = ""
