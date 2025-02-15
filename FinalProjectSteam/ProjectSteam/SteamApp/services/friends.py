"""This module contains the services related to the friend relations in the database."""

from typing import List, Optional
from fastapi import APIRouter, HTTPException

from DataAccessObjects.friend_data import FriendData
from DataAccessObjects.user_data import UserData
from crudOperations.friend import FriendsCRUD

from connections.db_connection import MySQLDatabaseConnection

router = APIRouter()
conn = MySQLDatabaseConnection()
crud = FriendsCRUD(conn)

@router.post("/friend/create", response_model=str)
def create(data: FriendData):
    """This service creates a new friend reference in the database.
    Remember that the friend data must have the specified structure."""
    try:
        isFriend = crud.is_friend(data.user_id, data.friend_id)
        if isFriend:
            raise HTTPException(status_code=400, detail="User is already friend of this user.")
        elif data.user_id == data.friend_id:
            raise HTTPException(status_code=400, detail="User cannot be friend of itself.")
        result = crud.create(data)
        if result == 0:
            return f"Friendship created with id: {data.user_id} and {data.friend_id}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.delete("/friend/delete/{user_id}/{friend_id}", response_model=bool)
def delete(user_id: int, friend_id: int):
    """This service deletes a friend reference from the database based on the user id and friend id."""
    try:
        crud.delete(user_id, friend_id)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/friend/get_all", response_model=List[FriendData])
def get_all():
    """This service gets all the friends references data."""
    return crud.get_all()

@router.get("/friend/get_by_user_id/{user_id}", response_model=List[UserData])
def get_by_user_id(user_id: int):
    """This service gets all the users info from the repository based on the user id in the friends table."""
    return crud.get_by_user_id(user_id)
@router.get("/friend/is_friend/{user_id}/{friend_id}", response_model=bool)
def is_friend(user_id: int, friend_id: int):
    """This service checks if the user is already friends with the friend id."""
    return crud.is_friend(user_id, friend_id)