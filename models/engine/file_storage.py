#!/usr/bin/python3
"""Defines a class that serializes instances to a JSON file and
deserializes JSON file to instances:
"""
# imports
import json
from models.base_model import BaseModel


class FileStorage:
    """Class for file storage"""
    __file_path = "storage.json"
    """path to the JSON file"""

    __objects = {}
    """Stores all basemodel objects"""

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Adds created object to objects dictionary.
        Key format <obj class name>.id in __objects

        Args:
            obj (BaseModel): Object to be added
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """"Update objects json stored in json
        Serializes __objects to the JSON file (path: __file_path)
        """
        # Convert __objects dictionary to JSON
        # json_dumps cannot convert objecst to JSON use each objects to_dict()
        # method
        dictionary_objects = {}
        for key, value in self.__objects.items():
            dictionary_objects[key] = value.to_dict()

        # Open file for writing and close automatically
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(dictionary_objects))

    def reload(self):
        """"Deserializes the JSON file to __objects if file exists"""
        # Open file for reading and close automatically
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                # Convert JSON to Dictionary
                dictionary_objects = json.loads(file.read())
                
                # Loop dictionary, create objects and add them to __objects list
                for key, value in dictionary_objects.items():
                    obj = BaseModel(**value)
                    self.new(obj) # Add to objects list

        #Raised when a file or directory is requested but doesn’t exist.
        except FileNotFoundError:
            # Do nothing
            pass
