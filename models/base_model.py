#!/usr/bin/python3
"""This is the super basemodel module

This is the super basemodel module. It contains the BaseModel class,
which provides functionality for instantiating, serializing,
deserializing, and storing objects.

Classes:
    BaseModel: The base model class.
"""

import uuid
import datetime
import json
from models import storage


class BaseModel:
    """The BaseModel class represents the base model for other classes.

    This class provides the core functionality for instantiating objects,
    managing creation and update times, and converting objects to dictionary
    representations.

    Methods:
        __init__: Initializes a new BaseModel instance.
        __str__: Returns a string representation of the BaseModel instance.
        save: Saves the BaseModel instance.
        to_dict: Converts the BaseModel instance to a dictionary.

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The timestamp of instance creation.
        updated_at (datetime): The timestamp of instance update.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        if kwargs:
            if '__class__' in kwargs:
                # Remove __class__ key if present
                del kwargs['__class__']
            for key, value in kwargs.items():
                # Converts string to datetime
                if key in ('created_at', 'updated_at'):
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

        # Here i will pop the __class__ key/value and allow both created_at
        # & updated_at be in the normal datetime format. then pass what's
        # left of the dictionary as argument of the constructor

    def __str__(self):
        """Returns a string representation of the BaseModel instance.

        Returns:
            str: The string representation of the BaseModel instance.
        """

        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves the recent date.

        Updates the updated_at attribute to the current date and time.
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Converts the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseModel instance.
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
