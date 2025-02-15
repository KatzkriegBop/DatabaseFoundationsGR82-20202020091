"""This module defines the friend data object"""
from pydantic import BaseModel, Field

class FriendData(BaseModel):
    """This class represents a friend data object"""
    user_id: int
    friend_id: int