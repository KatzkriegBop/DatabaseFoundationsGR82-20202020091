"""This module contains the services related to the friend relations in the database."""

from typing import List
from fastapi import APIRouter, HTTPException

from DataAccessObjects.library_data import LibraryData
from DataAccessObjects.user_data import UserData
from DataAccessObjects.game_data import GameData
from crudOperations.library import LibraryCRUD

from connections.db_connection import MySQLDatabaseConnection

router = APIRouter()
conn = MySQLDatabaseConnection()
crud = LibraryCRUD(conn)

@router.post("/library/create", response_model=str)
def create(data: LibraryData):
    """This service creates a new friend reference in the database.
    Remember that the friend data must have the specified structure."""
    try:
        isFriend = crud.has_game(data.user_id, data.game_id)
        if isFriend:
            raise HTTPException(status_code=400, detail="User already has this game.")
        result = crud.create(data)
        if result == 0:
            return f"User with id {data.user_id} bought the game with id {data.game_id}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.delete("/library/delete/{user_id}/{game_id}", response_model=bool)
def delete(user_id: int, game_id: int):
    """This service deletes a friend reference from the database based on the user id and friend id."""
    try:
        crud.delete(user_id, game_id)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

@router.get("/library/get_all", response_model=List[LibraryData])
def get_all():
    """This service gets all the library references data."""
    return crud.get_all()

@router.get("/library/get_games_by_user_id/{user_id}", response_model=List[GameData])
def get_games_by_user_id(user_id: int):
    """This service gets all the games info from the repository based on the user id in the library table."""
    return crud.get_games_by_user_id(user_id)

@router.get("/library/has_game/{user_id}/{game_id}", response_model=bool)
def has_game(user_id: int, game_id: int):
    """This service checks if the user has already this game."""
    return crud.has_game(user_id, game_id)

@router.get("/library/get_user_by_games_id/{game_id}", response_model=List[UserData])
def get_user_by_games_id(game_id: int):
    """This service gets all the users who has the game in the library table."""
    return crud.get_user_by_games_id(game_id)