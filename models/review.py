#!/usr/bin/python3
"""This module is the Review module
    it contains a subclass of BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents review.
    This is a subclass of BaseModel

    Attributes:
        state_id:
        name:
    """
    place_id = ""
    user_id = ""
    text = ""
