"""This module defines the game data object"""

from datetime import datetime

from pydantic import BaseModel,Field
from typing import Union


class GameData(BaseModel):
    """This class represents a game data object"""
    game_id: int
    game_name: str
    genre_id: Union[int, str]
    developer: str
    release_date: datetime = Field(default_factory=datetime.now)
    cost: float
