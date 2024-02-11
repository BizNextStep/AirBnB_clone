#!/usr/bin/python3
<<<<<<< HEAD


"""Initialize the engine package."""
from .file_storage import FileStorage
=======
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage
>>>>>>> ba1caa812b1462158338e37d86213b92e332b9d0


storage = FileStorage()
storage.reload()
