#!/usr/bin/env python3

"""
    This module contains a class to test \
    the base model class
"""
import os
import time
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

    def test_noarg_init(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_id_randomness(self):
        """
            test to confirm that id values are random
        """

        new_uid = BaseModel()
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

    def test_to_dict_contains_added_attributes(self):
        class_instance = BaseModel()
        class_instance.name = "ALX"
        class_instance.number = 21
        self.assertIn("name", class_instance.to_dict())
        self.assertIn("number", class_instance.to_dict())

    def test_to_dict_datetime_attributes(self):
        class_instance = BaseModel()
        class_dict = class_instance.to_dict()
        self.assertEqual(str, type(class_dict["created_at"]))
        self.assertEqual(str, type(class_dict["updated_at"]))

    def test_save_one(self):
        class_instance = BaseModel()
        time.sleep(0.03)
        time_of_first_update = class_instance.updated_at
        class_instance.save()
        self.assertLess(time_of_first_update, class_instance.updated_at)

    def test_save_updates_file(self):
        class_instance = BaseModel()
        class_instance.save()
        class_instance_id = "BaseModel." + class_instance.id
        with open("objects.json", "r") as f:
            self.assertIn(class_instance_id, f.read())
