#!/usr/bin/python3
""" This class inherits from BaseModel """
from models.base_model import BaseModel

class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new State instance."""
        super().__init__(*args, **kwargs)
