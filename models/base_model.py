#!/usr/bin/python3
"""This is the super basemodel module"""

import uuid
import datetime


class BaseModel:
    """This is the super basemodel class.
    It contains the init constructor, str, save, to_dict methods
    it instantiates, serializes, deserializes and stores"""

    def __init__(self, *args, **kwargs):
        """The constructor, accepts both *args and **kwargs"""

        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']  # Remove __class__ key if present
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):  # string to d_t
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

        # self.__dict__.update(kwargs)
        # self.__dict__.update(kwargs)
        # self.__dict__.pop('__class__', None)

        # created_at_str = self.__dict__['created_at']
        # updated_at_str = self.__dict__['updated_at']
        # created_dt = datetime.datetime.fromisoformat(created_at_str)
        # updated_dt = datetime.datetime.fromisoformat(updated_at_str)
        # self.__dict__['created_at'] = created_dt
        # self.__dict__['updated_at'] = updated_dt

        """Here i will pop the __class__ key/value and allow both created_at
        & updated_at be in the normal datetime format. then pass what's
        left of the dictionary as argument of the constructor"""

        """if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)"""

    def __str__(self):
        """Return a string representation of the class"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves the recent date"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Converts to a dictionary representation"""
        # self.__dict__['__class__'] = self.__class__.__name__
        # return self.__dict__
        # print(self.__dict__)
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
