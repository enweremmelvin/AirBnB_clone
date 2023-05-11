#!/usr/bin/env python3

"""
    This module contains a class <TestSaveReload> that \
    runs unittests on the (save, new, reload) methods of the \
    file_storage module
"""

import os
import json
import unittest
from models import storage
from models.base_model import BaseModel


class TestSaveReload(unittest.TestCase):
    """
        run tests to discern that the implmentation of \
        <5. Store first object> works
    """

    def test_file_creation(self):
        """
            test if object file is created
        """

        new_obj = BaseModel()
        new_obj.name = "John Doe"
        new_obj.age = 35

        new_obj.save()
        check_file = os.path.exists("objects.json")

        self.assertEqual(check_file, True)

    def test_file_content(self):
        """
            test that object file gets populated with values \
            when the instance save method is called
        """

        new_obj = BaseModel()
        new_obj.name = "John Doe"
        new_obj.age = 35

        new_obj.save()

        file_content = None

        with open("objects.json", mode="r", encoding="utf-8") as file_handle:
            file_content = file_handle.read()

        self.assertNotEqual(file_content, None)
