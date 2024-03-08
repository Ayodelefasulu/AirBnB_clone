#!/usr/bin/python3
""" This class inherits from BaseModel """
from models.base_model import BaseModel

class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance."""
        super().__init__(*args, **kwargs)
