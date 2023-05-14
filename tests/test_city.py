#!/usr/bin/python3

"""Defines unittests for models/city.py """

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    def test_no_args(self):
        """
            test no arguments passed
        """

        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """
            test if new instance is stored
        """

        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """
            test is id is public attribute
        """

        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """
            test if created at is a public datetime \
            attribute
        """

        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """
            test of updated at is a public datetime \
            attribute
        """

        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """
            test if id ia a public class attribute
        """

        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_name_is_public_class_attribute(self):
        """
            test if name is a public class attribute
        """

        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_two_cities_unique_ids(self):
        """
            test the unique id of two instances of city
        """

        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_cities_different_created_at(self):
        """
            test that two city instances have different created \
            at values
        """

        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_two_cities_different_updated_at(self):
        """
            test if two cities have different updated at values
        """

        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        """
            test str representation of class
        """

        date_time = datetime.today()
        date_time_repr = repr(date_time)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = date_time
        citystr = city.__str__()
        self.assertIn("[City] (123456)", citystr)
        self.assertIn("'id': '123456'", citystr)
        self.assertIn("'created_at': " + date_time_repr, citystr)
        self.assertIn("'updated_at': " + date_time_repr, citystr)

    def test_args_unused(self):
        """
            test unused arguments
        """

        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
            test instance creation with kwargs
        """

        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, date_time)
        self.assertEqual(city.updated_at, date_time)

    @classmethod
    def setUp(self):
        """
            class setup method
        """

        try:
            os.rename("objects.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """
            class tear down method
        """

        try:
            os.remove("objects.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "objects.json")
        except IOError:
            pass

    def test_one_save(self):
        """
            test if an instances attributes are saved to file
        """

        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_two_saves(self):
        """
            test if the attributes of two instances are saved \
            to file
        """

        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        second_updated_at = city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        city.save()
        self.assertLess(second_updated_at, city.updated_at)

    def test_save_with_arg(self):
        """
            test the save method with arguments
        """

        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        """
            test if the save method actually updates the file
        """

        city = City()
        city.save()
        cityid = "City." + city.id
        with open("objects.json", "r") as f:
            self.assertIn(cityid, f.read())

    def test_to_dict_type(self):
        """
            test the type of the return value of to dict
        """

        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
            test if to dict contains the right keys
        """

        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """
            test if to dict contains added attributes
        """

        city = City()
        city.middle_name = "Holberton"
        city.my_number = 98
        self.assertEqual("Holberton", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """
            test if type of time attributes are str
        """

        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        """
            test the output of to dict
        """

        date_time = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """
            test the contents of to dict against class method \
            __dict__
        """

        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_with_arg(self):
        """
            test how to dict behaves when passed args
        """

        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)
