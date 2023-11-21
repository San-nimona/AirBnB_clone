#!/usr/bin/python3
"""
Functions and Classes:
    class City(BaseModel):
"""


from models.base_model import BaseModel


class City(BaseModel):
    """Representing a city"""

    state_id = ""
    name = ""
