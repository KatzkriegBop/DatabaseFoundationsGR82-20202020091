"""This module defines the user data object."""
from datetime import datetime
from pydantic import BaseModel, Field

class UserData(BaseModel):
    """This class represents an user data object"""
    steam_id: int = Field(default=None)
    username: str
    phone: int
    password: str
    email: str
    country: str
    creation_date: datetime = Field(default_factory=datetime.now)
