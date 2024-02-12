#!/usr/bin/python3

import uuid
import datetime
from models import storage
import json


class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']  # Remove __class__ key if present
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):  # Convert string to d_t
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

       # self.__dict__.update(kwargs)
       # self.__dict__.update(kwargs)
       # self.__dict__.pop('__class__', None)

        #created_at_str = self.__dict__['created_at']
        #updated_at_str = self.__dict__['updated_at']
        #created_dt = datetime.datetime.fromisoformat(created_at_str)
        #updated_dt = datetime.datetime.fromisoformat(updated_at_str)
        #self.__dict__['created_at'] = created_dt
        #self.__dict__['updated_at'] = updated_dt

        """Here i will pop the __class__ key/value and then allow both created_at
        & updated_at to be in the normal datetime format. then i will pass what's
        left of the dictionary as argument of the constructor"""

        """if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)"""

    def __str__(self):
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
       # self.__dict__['__class__'] = self.__class__.__name__
       # return self.__dict__
       # print(self.__dict__)
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
