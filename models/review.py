#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents review."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
