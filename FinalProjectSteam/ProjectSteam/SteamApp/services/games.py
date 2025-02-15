"""This module contains the services related to the games in the database."""

from typing import List, Optional
from fastapi import APIRouter, HTTPException

from DataAccessObjects.game_data import GameData
from DataAccessObjects.genre_data import GenreData
from crudOperations.game import GamesCRUD

from connections.db_connection import MySQLDatabaseConnection


router = APIRouter()
conn = MySQLDatabaseConnection()
crud = GamesCRUD(conn)

@router.post("/game/create", response_model=int)
def create(data: GameData):
    """This service creates a new game in the database.
    Remember that the game data must have the specified structure."""
    try:
        # Check if a game with the same developer name and game name already exists
        existing_games = crud.get_all()
        for game in existing_games:
            if game['developer'] == data.developer and game['game_name'] == data.game_name:
                raise HTTPException(status_code=400, detail="Game with the same developer name and game name already exists")
        
        return crud.create(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.put("/game/update/{id_}", response_model=bool)
def update(id_: int, data: GameData):
    """This service updates the user data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.delete("/game/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a user from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.get("/game/get_by_id/{id_}", response_model=Optional[GameData])
def get_by_id(id_: int):
    """This service gets a game from the database based on its id."""
    user = crud.get_by_id(id_)
    if user == 'Game not found':
        raise HTTPException(status_code=404, detail="Game not found")
    return user


@router.get("/game/get_all", response_model=List[GameData])
def get_all():
    """This service gets all the games from the database."""
    return crud.get_all()

@router.get("/game/get_by_genre", response_model=List[GameData])
def get_by_genre(genre_id: int):
    """This service gets all the games from the database based on the genre."""
    return crud.get_by_genre(genre_id)
@router.get("/game/get_by_developer", response_model=List[GameData])
def get_by_developer(developer: str):
    """This service gets all the games from the database based on the developer."""
    return crud.get_by_dev(developer)

@router.get("/game/get_by_name", response_model=List[GameData])
def get_by_name(game_name: str):
    """This service gets all the games from the database based on the game name."""
    return crud.get_by_name(game_name)

@router.get("/game/get_genres", response_model=List[GenreData])
def get_genres():
    """This service gets all the genres from the database."""
    return crud.get_genres()
