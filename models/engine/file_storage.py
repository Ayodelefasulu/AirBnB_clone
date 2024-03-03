#!/usr/bin/python3
"""This is filestorage module"""


import json
import os
# from models.base_model import BaseModel


class FileStorage:
    """This is filestorage class"""
    __file_path = "file.json"
    __objects = {}
    __class_names = set()  # Store class names here

    def all(self):
        """This method returns all objects"""
        return self.__objects
        # return type(self).__objects
        # print("all is here")

    def new(self, obj):
        """This method creates new obj"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

        # Update class names
        self.__class_names.add(obj.__class__.__name__)

    def save(self):
        """It saves objects to json file by serializing"""
        with open(self.__file_path, 'w') as f:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

        """ serialized_objs = {}
            for key, value in self.__objects.items():
                serialized_objs[key] = value.to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(serialized_objs, file)"""

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):  # Check if file exists
            if os.path.getsize(self.__file_path) > 0:
                with open(self.__file_path, 'r') as f:
                    data = json.load(f)

           # for key, value in data.items():
                    #obj = self.class_name(**value)  # Recreate BaseModel object
            #        self.__objects[key] = obj
                # Add more conditions for other classes if needed
        else:
            return
        """
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except Exception:
                pass
        """
        # Update class names
        self.__class_names = {key.split('.')[0] for key in data.keys()}
