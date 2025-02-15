"""This module defines the genre data object"""
from pydantic import BaseModel

class GenreData(BaseModel):
    """This class represents a genre data object"""
    genre_id: int = -1
    genre_name: str