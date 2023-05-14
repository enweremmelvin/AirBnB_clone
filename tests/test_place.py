#!/usr/bin/python3

"""Defines unittests for models/place.py. """

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""

    def test_no_args_instantiates(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """ placeholder docstring - to be properly docced """

        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """ placeholder docstring - to be properly docced """

        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place))
        self.assertNotIn("city_id", place.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)

    def test_name_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

    def test_description_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place))
        self.assertNotIn("desctiption", place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(place))
        self.assertNotIn("number_bathrooms", place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)

    def test_two_placeaces_unique_ids(self):
        """ placeholder docstring - to be properly docced """

        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_two_placeaces_different_created_at(self):
        """ placeholder docstring - to be properly docced """

        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_two_placeaces_different_updated_at(self):
        """ placeholder docstring - to be properly docced """

        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_str_representation(self):
        """ placeholder docstring - to be properly docced """

        date_time = datetime.today()
        date_time_repr = repr(date_time)
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = date_time
        placestr = place.__str__()
        self.assertIn("[Place] (123456)", placestr)
        self.assertIn("'id': '123456'", placestr)
        self.assertIn("'created_at': " + date_time_repr, placestr)
        self.assertIn("'updated_at': " + date_time_repr, placestr)

    def test_args_unused(self):
        """ placeholder docstring - to be properly docced """

        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """ placeholder docstring - to be properly docced """

        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        place = Place(id="345", created_at=date_time_iso,
                      updated_at=date_time_iso)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, date_time)
        self.assertEqual(place.updated_at, date_time)

    @classmethod
    def setUp(self):
        """ placeholder docstring - to be properly docced """

        try:
            os.rename("objects.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        """ placeholder docstring - to be properly docced """

        try:
            os.remove("objects.json")
        except IOError:
            pass
        try:
            os.rename("temp", "objects.json")
        except IOError:
            pass

    def test_one_save(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_two_saves(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        second_updated_at = place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        place.save()
        self.assertLess(second_updated_at, place.updated_at)

    def test_save_with_arg(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_updates_file(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        place.save()
        placeid = "Place." + place.id
        with open("objects.json", "r") as f:
            self.assertIn(placeid, f.read())

    def test_to_dict_type(self):
        """ placeholder docstring - to be properly docced """

        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        place.middle_name = "ALX"
        place.my_number = 98
        self.assertEqual("ALX", place.middle_name)
        self.assertIn("my_number", place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        """ placeholder docstring - to be properly docced """

        date_time = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

    def test_to_dict_with_arg(self):
        """ placeholder docstring - to be properly docced """

        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)
