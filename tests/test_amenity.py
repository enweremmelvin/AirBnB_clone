#!/usr/bin/python3

"""
    module for testing the amenity class
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""

    def test_no_args(self):
        """
            test when no args is passed to amenity
        """

        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_in_objects(self):
        """
            test new instance in objects
        """

        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_str(self):
        """
            test is the id is a string
        """

        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime(self):
        """
            test is created at is a datetime object
        """

        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        """
            test if updated at is a datetime object
        """

        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """
            test if name is a public class attribute
        """

        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        """
            test the equailty of the unique ids of two \
            instances of the amenity class
        """

        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        """
            test if two amenities have different created at \
            values
        """

        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        """
            teest if two amenitites have different updated at \
            values
        """

        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        """
            test the str representation of an instance
        """

        date_time = datetime.today()
        date_time_repr = repr(date_time)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = date_time
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + date_time_repr, amstr)
        self.assertIn("'updated_at': " + date_time_repr, amstr)

    def test_args_unused(self):
        """
            test if None is not initialized as an attribute
        """

        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""

        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, date_time)
        self.assertEqual(am.updated_at, date_time)

    @classmethod
    def setUp(self):
        """
            class setup method
        """

        try:
            os.rename("objects.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        """
            class teardown method
        """

        try:
            os.remove("objects.json")
        except IOError:
            pass
        try:
            os.rename("temp", "objects.json")
        except IOError:
            pass

    def test_one_save(self):
        """
            test the save method of an instance
        """

        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        """
            test the save method of two instances
        """

        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        """
            test save with arguments
        """

        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        """
            test that updates are saved to file
        """

        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("objects.json", "r") as f:
            self.assertIn(amid, f.read())

    def test_to_dict_type(self):
        """
            test to dict return type
        """

        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
            test that to dict contains the right values
        """

        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """
            test that to dict contains added attributes
        """

        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """
            test that to dict datetime attributes are strings
        """

        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        """
            test the output of to dict
        """

        date_time = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """
            test that to dict is not equal to the return
            value of the __dict__ method
        """

        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        """
            test to dict with arguments
        """

        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)
