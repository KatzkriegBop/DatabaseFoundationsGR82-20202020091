from typing import List
from DataAccessObjects.user_data import UserData
from DataAccessObjects.game_data import GameData
from connections import db_connection
from DataAccessObjects.library_data import LibraryData

class LibraryCRUD:
    """This class is responsible for performing CRUD operations on the library table.

    Attributes:
        database_connection (db_connection): The database connection
    
    methods:
        create: Creates a new library in the database.
        delete: Deletes the library from the database.
        has_game: Checks if user already has the game.
        get_all: Gets all the library data.
        get_games_by_user_id: Gets all the games of a user based on the user id.
        get_users_from_game_id: Gets all the users who has certain game.
    """
    
    def __init__(self, db_connection: db_connection):
        self.database_connection = db_connection
        self.database_connection.connect()
    
    def create(self, data: LibraryData) -> int:
        """This method creates a new library in the database.
        args:
            data (Library): The library data.
        Returns:
            The auto-generated id of the new library
        """
        query = """
            INSERT INTO SteamLibrary(UserID, GameID)
            VALUES (%s, %s)
        """
        values = (data.user_id, data.game_id)
        return self.database_connection.create(query, values)
    
    def delete(self, user_id: int, game_id: int):
        """This method deletes the library reference from the database.
        args:
            user_id (int): The user id to be deleted.
            game_id (int): The friend id of the game to be deleted.
        """
        query = """DELETE FROM SteamLibrary 
            WHERE (UserID = %s AND GameID = %s) 
            OR (UserID = %s AND GameID = %s)
            """
        values = (user_id, game_id, game_id, user_id)
        self.database_connection.delete(query, values)

    def has_game(self, user_id: int, game_id: int) -> bool:
        """This method checks if the user has this game already.
        args:
            user_id (int): The user id.
            game_id (int): The game id.
        Returns:
            True if the user already has the game, False otherwise.
        """
        query = """SELECT COUNT(*) FROM SteamLibrary 
                WHERE (UserID = %s AND GameID = %s)
                """
        values = (user_id, game_id,game_id,user_id)
        result = self.database_connection.get_one(query, values)
        if result and result['COUNT(*)'] > 0:
                    return True
        return False
    
    def get_all(self) -> List[LibraryData]:
        """This method gets all the friends data.
        Returns:
            A list of all the friends data.
        """
        query = """SELECT * FROM SteamLibrary"""
        items = self.database_connection.get_many(query)
        results = [
                {
                    'user_id': row[0],
                    'game_id': row[1]
                }
                for row in items
            ]
        return results
    def get_games_by_user_id(self, id_: int) -> GameData:
        """This method gets a game from the repository based on the id.
        args:
            id (int): The id of the game to get.
        Returns:
            The game data.
        """
        query = """
            SELECT * 
            FROM SteamLibrary
            JOIN Game ON SteamLibrary.GameID = Game.Id
            WHERE SteamLibrary.UserID = %s;
            """
        values = (id_,)
        items = self.database_connection.get_many(query,values)
        results = [
                {
                    'game_id': row[2],
                    'game_name': row[3],
                    'genre_id': row[4],
                    'developer': row[5],
                    'release_date': row[6],
                    'cost': row[7]
                }
                for row in items
            ]
        return results
    def get_user_by_games_id(self, id_: int) -> UserData:
        """This method gets a game from the repository based on the id.
        args:
            id (int): The id of the game to get.
        Returns:
            The game data.
        """
        query = """
            SELECT * 
            FROM SteamLibrary
            JOIN User ON SteamLibrary.UserID = User.SteamID
            WHERE SteamLibrary.GameID = %s;
            """
        values = (id_,)
        items = self.database_connection.get_many(query,values)
        results = [
                {
                    'steam_id': row[2],
                    'username': row[3],
                    'phone': row[4],
                    'email': row[5],
                    'password': row[6],
                    'country': row[7],
                    'creation_date': row[8],
                    'status': row[9]
                }
                for row in items
            ]
        return results
    