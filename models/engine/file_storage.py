#!/usr/bin/python3
"""FileStorage Module

This module provides FileStorage class for serializing & deserializing objects
to and from a JSON file.

Classes:
    FileStorage: A class for managing storage of objects in a JSON file.

"""
import json
import os
#from models.user import User


class FileStorage():
    """A class for managing storage of objects in a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing objects stored in memory.

    Methods:
        all(self): Returns the dictionary of objects.
        new(self, obj): Adds a new object to the dictionary.
        save(self): Saves the current state of the dictionary to the JSON file.
        reload(self): Loads data from the JSON file into the dictionary.

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary.

        Args:
            obj: The object to be added.

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the current state of the dictionary to the JSON file."""
        filepath = os.path.join(os.getcwd(), self.__file_path)
        with open(filepath, 'w') as f:
            """obj_dict = {}
            for key, value in self.__objects.items():
                if isinstance(value, BaseModel):
                    obj_dict[key] = value.to_dict()
                else:
                    obj_dict[key] = value"""
            obj_dict =\
                {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f, indent=4, separators=(',', ':'))
            f.write('\n')

    def reload(self):
        """Load data from the JSON file into the dictionary."""
        filepath = os.path.join(os.getcwd(), self.__file_path)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    data = f.read()
                    if data:
                        loaded_data = json.loads(data)
                        from models.base_model import BaseModel
                        for key, value in loaded_data.items():
                            self.__objects[key] = BaseModel(**value)

                    # data = json.load(f)
                    # self.__objects = {}
                    # for key, value in data.items():
                    #     class_name, obj_id = key.split('.')
                    #     self.__objects[key] = globals()[class_name](**value)
            except FileNotFoundError as e:
                print(f"Error: File '{filepath}' not found.")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("JSON file does not exist")
