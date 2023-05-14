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

    def test_created_at_is_datetime(self):
        """
            test that instance attribute <created_at> and <updated_at> \
            are datetime objects
        """

        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_time_value(self):
        """
            test if time values are instantiated \
            and are not none
        """

        class_instance = BaseModel()

        self.assertNotEqual(class_instance.created_at, None)
        self.assertNotEqual(class_instance.updated_at, None)

    def test_noarg_init(self):
        """
            test type of object initialized without
        """

        self.assertEqual(BaseModel, type(BaseModel()))

    def test_str_representation(self):
        """
            test that the string representation returns the correct \
            values
        """

        date_time = datetime.now()
        date_time_repr = repr(date_time)
        base_model = BaseModel()
        base_model.id = "012345"
        base_model.created_at = date_time
        base_model.updated_at = date_time
        base_model_str = base_model.__str__()
        self.assertIn("[BaseModel] (012345)", base_model_str)
        self.assertIn("'id': '012345'", base_model_str)
        self.assertIn("'created_at': " + date_time_repr, base_model_str)
        self.assertIn("'updated_at': " + date_time_repr, base_model_str)

    def test_id_is_str(self):
        """
            test type of id
        """

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
        """
            test is the to_dict() of a method contains custom \
            added attributes
        """

        class_instance = BaseModel()
        class_instance.name = "ALX"
        class_instance.number = 21
        self.assertIn("name", class_instance.to_dict())
        self.assertIn("number", class_instance.to_dict())

    def test_to_dict_output(self):
        """
            test the output of the to_dict() method
        """

        date_time = datetime.now()
        base_model = BaseModel()
        base_model.id = "012345"
        base_model.created_at = base_model.updated_at = date_time
        check_dict = {
            'id': '012345',
            '__class__': 'BaseModel',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), check_dict)

    def test_to_dict_datetime_attributes(self):
        """
            test the datetime attribute types of <created_at> \
            and <updated_at> -> ideally str in the retun value of \
            to_dict()
        """

        class_instance = BaseModel()
        class_dict = class_instance.to_dict()
        self.assertEqual(str, type(class_dict["created_at"]))
        self.assertEqual(str, type(class_dict["updated_at"]))

    def test_to_dict_with_arg(self):
        """
            test that to_dict() raises an error when passed an argument
        """

        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)

    def test_save_one(self):
        """
            test that the updated_at attribute works as intended
        """

        class_instance = BaseModel()
        time.sleep(0.03)
        time_of_first_update = class_instance.updated_at
        class_instance.save()
        self.assertLess(time_of_first_update, class_instance.updated_at)

    def test_save_with_arg(self):
        """
            test that the save method returns a TypeError when passed \
            <None> as an argument
        """

        class_instance = BaseModel()
        with self.assertRaises(TypeError):
            class_instance.save(None)

    def test_save_updates_file(self):
        """
            test that a class gets saved correctly to the json file \
            NOTE:: create a class attribute __file_name to hold name \
            + -> of json file -> dynamic > static
        """

        class_instance = BaseModel()
        class_instance.save()
        class_instance_id = "BaseModel." + class_instance.id
        with open("objects.json", "r") as f:
            self.assertIn(class_instance_id, f.read())

    @classmethod
    def setUp(self):
        """
            setUp method for class instance methods
        """

        try:
            os.rename("objects.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """
            tearDown method
        """

        try:
            os.remove("objects.json")
        except IOError:
            pass
        try:
            os.rename("temp", "objects.json")
        except IOError:
            pass

    def test_save_updates_file(self):
        """
            test that <class_name>.<class_id> gets added correctly \
            to the json file
        """

        base_model = BaseModel()
        base_model.save()
        bid = "BaseModel." + base_model.id
        with open("objects.json", "r") as f:
            self.assertIn(bid, f.read())
