#!/usr/bin/python3
""" This class inherits from BaseModel """
from models.base_model import BaseModel

class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity instance."""
        super().__init__(*args, **kwargs)
