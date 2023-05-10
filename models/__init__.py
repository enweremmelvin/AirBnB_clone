#!/usr/bin/env python3

"""
    this module makes this directory into a python package
"""

from models.engine.file_storage import FileStorage


# -> create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()
