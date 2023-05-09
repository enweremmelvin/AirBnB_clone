#!/usr/bin/env python3

"""
    This module contains a class to test \
    the base model class
"""

import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        test various conditions on the BaseModel
        *** ensure the BaseModel class works as intended
    """

    def test_time_value(self):
        """
            test if time values are instantiated \
            and are not none
        """

        class_instance = BaseModel()

        self.assertNotEqual(class_instance.created_at, None)
        self.assertNotEqual(class_instance.updated_at, None)

    def test_id_randomness(self):
        """
            test to confirm that id values are random
        """

        new_uid = uuid.uuid4()
        class_instance = BaseModel()

        self.assertNotEqual(new_uid, class_instance.id)

    def test_to_dict_method(self):
        """
            test if to_dict() method returns a dictionary
        """

        class_instance = BaseModel()
        dict_val = class_instance.to_dict()

        self.assertEqual(type(dict_val), dict)

    def test_dict_values(self):
        """
            test that dictionary representation contains \
            the right value
        """

        class_instance = BaseModel()
        dict_val = class_instance.to_dict()

        attr_list = ["__class__", "id", "created_at", "updated_at"]

        for value in attr_list:
            check = value in dict_val
            self.assertEqual(check, True)
