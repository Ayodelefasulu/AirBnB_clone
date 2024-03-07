#!/usr/bin/python3
""" This module is a subclass of BaseModel

    class: User - inherit from BaseModel class

    attr: email, password, first_name, last_name
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel.

        attr: email, password, first_name, last_name

        constructor: __init__, args and kwargs
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
