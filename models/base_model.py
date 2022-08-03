#!/usr/bin/python3
"""Defines a base model class.

This class defines all common attributes/methods for other classes.
"""
# Imports
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Represents the "base" for all other classes."""

    # kwargs is a dictionary
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel/ Instance

        Args:
            id (int): Unique id for each BaseModel
            created_at: Date of object creation
            updated_at: Date of object change
        """
        if kwargs:
            # Create from dictionary, Loop dictionary key and values
            for key, value in kwargs.items():
                # Set object attributes dynamically using setattr function
                if(key == "__class__"):
                    continue

                # Convert isoformat string date to datetime object
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)
        else:
            # Create new instance
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            # Add to objects list for future storing
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute updated_at with
            the current datetime.
        """
        self.updated_at = datetime.now()

        # Update object in storage
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of
            the instance
        """
        # Create dictionary from all writable attributes of object
        dictionary = self.__dict__

        # Add class name to dictionary
        dictionary["__class__"] = self.__class__.__name__

        # Converted datetime to string object in ISO format
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        """Return the printable representation of model in the format
            print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}" \
            .format(self.__class__.__name__, self.id, self.__dict__)
