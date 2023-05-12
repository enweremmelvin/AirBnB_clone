#!/usr/bin/env python3

"""
    module that contains a class <Place> \
    that inherits from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
        class <Place> that inherits from BaseModel

        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list: \
        + it will be the list of Amenity.id later
    """

    # class attribute(s): Type <str>
    name = ""
    city_id = ""
    user_id = ""
    description = ""

    # class attribute(s): Type <int>
    max_guest = 0
    number_rooms = 0
    price_by_night = 0
    number_bathrooms = 0

    # class attribute(s): Type <float>
    latitude = 0.0
    longitude = 0.0

    # class attribute(s): Type <list>
    amenity_ids = []
