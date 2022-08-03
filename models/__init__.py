#!/usr/bin/python3
# import file_storage module
from models.engine.file_storage import FileStorage

# Storage object to handle persistnt data saving
storage = FileStorage()

# Reload information from storage
storage.reload()
