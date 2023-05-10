#!/usr/bin/env python3

"""
    This module contains a class <TestModelFromDict> that tests \
    the create model from dictionary functionality of the magic method \
    __init__ in BaseModel()
"""

import unittest
from models.base_model import BaseModel


class TestModelFromDict(unittest.TestCase):
    """
        subclass of unittest to test that the test model \
        from dict works functionality works

        For task: 4. Create BaseModel from dictionary
    """

    def test_object_creation(self):
        """
            test that the new object is created with attributes and values \
            of preceding object generated with the <to_dict()> instance method
        """

        new_obj = BaseModel()

        # instantiate instance attributes
        new_obj.age = 50
        new_obj.lname = "Doe"
        new_obj.fname = "John"

        dict_repr = new_obj.to_dict()

        # create new instance with values of attributes of \
        # the new_obj object
        copy_obj = BaseModel(**dict_repr)

        self.assertEqual(copy_obj.age, 50)
        self.assertEqual(copy_obj.lname, "Doe")
        self.assertEqual(copy_obj.fname, "John")

    def test_object_attributes(self):
        """
            test if the right attributes (not more/less than specified) \
            are in the new objects namespace
        """

        new_obj = BaseModel()

        # instantiate instance attributes
        new_obj.age = 50
        new_obj.lname = "Doe"
        new_obj.fname = "John"

        dict_repr = new_obj.to_dict()

        # create new instance with values of attributes of \
        # the new_obj object
        copy_obj = BaseModel(**dict_repr)

        copy_obj_dict = copy_obj.to_dict()
        key_list = list(dict_repr)

        for val in key_list:
            val1 = dict_repr[val]
            val2 = copy_obj_dict[val]

            self.assertEqual(val1, val2)
