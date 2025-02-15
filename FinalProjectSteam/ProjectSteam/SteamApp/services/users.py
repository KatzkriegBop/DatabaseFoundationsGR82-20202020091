"""This module contains the services related to the users in the database."""

from typing import List, Optional
from fastapi import APIRouter, HTTPException

from DataAccessObjects.user_data import UserData
from crudOperations.user import UsersCRUD

from connections.db_connection import MySQLDatabaseConnection


router = APIRouter()
conn = MySQLDatabaseConnection()
crud = UsersCRUD(conn)

@router.post("/user/create", response_model=int)
def create(data: UserData):
    """This service creates a new user in the database.
    Remember that the user data must have the specified structure."""
    try:
        existing_user_by_email = crud.get_by_email(data.email)
        existing_user_by_phone = crud.get_by_phone(data.phone)

        if (existing_user_by_email != 'No user found') or \
           (existing_user_by_phone != 'No user found'):
            raise HTTPException(status_code=400, detail="User with this email, phone, or username already exists.")
        
        return crud.create(data)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.put("/user/update/{id_}", response_model=bool)
def update(id_: int, data: UserData):
    """This service updates the user data in the database based on its id."""
    try:
        crud.update(id_, data)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.delete("/user/delete/{id_}", response_model=bool)
def delete(id_: int):
    """This service deletes a user from the database based on its id."""
    try:
        crud.delete(id_)
        return True
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.get("/user/get_by_id/{id_}", response_model=Optional[UserData])
def get_by_id(id_: int):
    """This service gets a user from the database based on its id."""
    user = crud.get_by_id(id_)
    if user == 'No user found':
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/user/get_all", response_model=List[UserData])
def get_all():
    """This service gets all the users from the database."""
    return crud.get_all()


@router.get("/user/get_by_name/{name}", response_model=List[UserData])
def get_by_name(name: str):
    """This service gets a user from the database based on its name."""
    return crud.get_by_name(name)


@router.get("/user/get_by_email/{email}", response_model=Optional[UserData])
def get_by_email(email: str):
    """This service gets a user from the database based on its email."""
    user = crud.get_by_email(email)
    if user == 'No user found':
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/user/get_by_country/{country}", response_model=List[UserData])
def get_by_country(country: str):
    """This service gets a user from the database based on its country."""
    return crud.get_by_country(country)

@router.get("/user/get_by_phone/{phone}", response_model=Optional[UserData])
def get_by_phone(phone: int):
    """This service gets a user from the database based on its phone."""
    user = crud.get_by_phone(phone)
    if user == 'No user found':
        raise HTTPException(status_code=404, detail="User not found")
    return user
