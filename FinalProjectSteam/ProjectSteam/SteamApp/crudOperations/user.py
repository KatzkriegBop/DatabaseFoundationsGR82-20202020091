"""This module defines the class to perform CRUD operations on the users table."""

from typing import List

from connections import db_connection
from DataAccessObjects.user_data import UserData

class UsersCRUD:
    """This class is responsible for performing CRUD operations
    on the users table.

    Attributes:
        database_connection (db_connection): The database connection

    Methods:
        create: Creates a new user in the database.
        update: Updates the user data in the database.
        delete: Deletes the user from the database.
        get_by_id: Gets an user from repository based on the id.
        get_all: Gets all the users data.
        get_by_name: Gets an user from repository based on the username.
        get_by_email: Gets an user from repository based on the email
        get_by_country: Gets an user from repository based on the country.
        get_by_phone: Gets an user from repository based on the phone.
    """

    def __init__(self, db_connection: db_connection):
        self.database_connection = db_connection
        self.database_connection.connect()

    def create(self, data: UserData) -> int:
        """This method creates a new user in the database.

        Args:
            data (UserData): The user data.

        Returns:
            The auto-generated id of the new user
        """
        query = """
            INSERT INTO User(UserName, UserPassword, Phone, Email, Country, CreationDate)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (data.username, data.password, data.phone, data.email, data.country, data.creation_date)
        return self.database_connection.create(query, values)

    def update(self, id_: int, data: UserData):
        """This method updates the user data in the database.

        Args:
            id (int): The id of the user to be updated.
            data (UserData): The user data.
        """
        query = """
            UPDATE User
            SET UserName = %s, UserPassword = %s, Email = %s, CreationDate = %s, Country = %s, Phone = %s
            WHERE SteamID = %s;
        """
        values = (data.username, data.password, data.email, data.creation_date, data.country, data.phone, id_)
        self.database_connection.update(query, values)

    def delete(self, id_: int):
        """This method deletes the user from the database.

        Args:
            id (int): The id of the user to be deleted.
        """
        query = """
                DELETE FROM User
                WHERE SteamID = %s;
            """
        values = (id_,)
        self.database_connection.delete(query, values)

    def get_by_id(self, id_: int) -> UserData:
        """This method gets a user from repository
        based on the id.

        Args:
            id_ (int): Id of the user

        Returns:
            The result of the query.
        """
        query = """
            SELECT *
            FROM User
            WHERE SteamID = %s;
            """
        values = (id_,)
        results = self.database_connection.get_one(query, values)
        user = {
            'steam_id': results.get('SteamID', None),
            'username': results.get('UserName', None),
            'phone': results.get('Phone', None),
            'email': results.get('Email', None),
            'password': results.get('UserPassword', None),
            'country': results.get('Country', None),
            'creation_date': results.get('CreationDate', None)
        }
        
        if not self.database_connection.get_one(query, values):
            return 'No user found'
        return user

    def get_all(self) -> List[UserData]:
        """This method allows to get all the users data.

        Returns:
            The result of the query.
        """
        query = """
            SELECT *
            FROM User;
            """
        items = self.database_connection.get_many(query)
        results = [
                {
                    'steam_id': row[0],
                    'username': row[1],
                    'phone': row[2],
                    'email': row[3],
                    'password': row[4],
                    'country': row[5],
                    'creation_date': row[6],
                    'status': row[7]
                }
                for row in items
            ]
        return results

    def get_by_name(self, name: str) -> List[UserData]:
        """This method gets a user from repository
        based on the name.

        Args:
            name (str): Name of the user

        Returns:
            The result of the query.
        """
        query = """
            SELECT *
            FROM User
            WHERE UserName LIKE %s;
        """
        values = (f"%{name}%",)
        items = self.database_connection.get_many(query, values)
        results = [
                {
                    'steam_id': row[0],
                    'username': row[1],
                    'phone': row[2],
                    'email': row[3],
                    'password': row[4],
                    'country': row[5],
                    'creation_date': row[6],
                    'status': row[7]
                }
                for row in items
            ]
        return results

    def get_by_email(self, email: str) -> UserData:
        """This method gets a user from repository
        based on the email.

        Args:
            email (str): Email of the user

        Returns:
            The user who matched the email.
        """
        query = """
            SELECT *
            FROM User
            WHERE Email = %s;
        """
        values = (email,)
        results = self.database_connection.get_one(query, values)
        user = {
            'steam_id': results.get('SteamID', None),
            'username': results.get('UserName', None),
            'phone': results.get('Phone', None),
            'email': results.get('Email', None),
            'password': results.get('UserPassword', None),
            'country': results.get('Country', None),
            'creation_date': results.get('CreationDate', None)
        }
        
        if not self.database_connection.get_one(query, values):
            return 'No user found'
        return user
    
    def get_by_country(self, country: str) -> List[UserData]:
        """This method gets a user from repository
        based on the country.

        Args:
            country (str): Country of the user

        Returns:
            The user who matched the country.
        """
        query = """
            SELECT *
            FROM User
            WHERE Country = %s;
        """
        values = (country,)
        items = self.database_connection.get_many(query, values)
        results = [
                {
                    'steam_id': row[0],
                    'username': row[1],
                    'phone': row[2],
                    'email': row[3],
                    'password': row[4],
                    'country': row[5],
                    'creation_date': row[6],
                    'status': row[7]
                }
                for row in items
            ]
        return results
    
    def get_by_phone(self, phone: int) -> UserData:
        """This method gets a user from repository
        based on the phone.

        Args:
            phone (int): Phone of the user

        Returns:
            The user who matched the phone.
        """
        query = """
            SELECT *
            FROM User
            WHERE Phone = %s;
        """
        values = (phone,)
        results = self.database_connection.get_one(query, values)
        user = {
            'steam_id': results.get('SteamID', None),
            'username': results.get('UserName', None),
            'phone': results.get('Phone', None),
            'email': results.get('Email', None),
            'password': results.get('UserPassword', None),
            'country': results.get('Country', None),
            'creation_date': results.get('CreationDate', None)
        }
        
        if not self.database_connection.get_one(query, values):
            return 'No user found'
        return user 
