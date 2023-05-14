#!/usr/bin/python3

"""Defines unittests for models/user.py. """

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""

    def test_no_args(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """ placeholder docstring - to be properly docced """

        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """ placeholder docstring - to be properly docced """

        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        """ placeholder docstring - to be properly docced """

        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """ placeholder docstring - to be properly docced """

        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        """ placeholder docstring - to be properly docced """

        date_time = datetime.today()
        date_time_repr = repr(date_time)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = date_time
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + date_time_repr, usstr)
        self.assertIn("'updated_at': " + date_time_repr, usstr)

    def test_args_unused(self):
        """ placeholder docstring - to be properly docced """

        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """ placeholder docstring - to be properly docced """

        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        us = User(id="345", created_at=date_time_iso, updated_at=date_time_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, date_time)
        self.assertEqual(us.updated_at, date_time)

    @classmethod
    def setUp(self):
        """ placeholder docstring - to be properly docced """

        try:
            os.rename("objects.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """ placeholder docstring - to be properly docced """

        try:
            os.remove("objects.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "objects.json")
        except IOError:
            pass

    def test_one_save(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_saves(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_with_arg(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        us.save()
        usid = "User." + us.id
        with open("objects.json", "r") as f:
            self.assertIn(usid, f.read())

    def test_to_dict_type(self):
        """ placeholder docstring - to be properly docced """

        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        us.middle_name = "ALX"
        us.my_number = 98
        self.assertEqual("ALX", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        """ placeholder docstring - to be properly docced """

        date_time = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        """ placeholder docstring - to be properly docced """

        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)
