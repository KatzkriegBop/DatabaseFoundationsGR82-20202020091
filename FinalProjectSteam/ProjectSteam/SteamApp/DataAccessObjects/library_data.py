"""This module defines the library data object"""
from pydantic import BaseModel

class LibraryData(BaseModel):
    """This class represents a library data object"""
    user_id: int
    game_id: int