#!/usr/bin/env python3
"""
create a unique FileStorage instance for your application

from file_storage import FileStorage

#FileStorage instance
storage = FileStorage()
#call the roload method on storage
storage.reload()

"""
"""Initializes the package"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
