"""This module defines the class to perform CRUD operations on the games table."""
from typing import List

from connections import db_connection
from DataAccessObjects.game_data import GameData

class GamesCRUD:
    """This class is responsible for performing CRUD operations
    on the games table.

    Attributes:
        database_connection (db_connection): The database connection

    Methods:
        create: Creates a new game in the database.
        update: Updates the games data in the database.
        delete: Deletes the game from the database.
        get_by_id: Gets a game from repository based on the id.
        get_all: Gets all the games data.
        get_by_name: Gets a game from repository based on the name.
        get_by_genre: Gets a game from repository based on the genre.
        get_by_dev: Gets a game from repository based on the dev.
    """
    def __init__(self, db_connection: db_connection):
        self.database_connection = db_connection
        self.database_connection.connect()

    def create(self, data: GameData) -> int:
        """This method creates a new game in the database.
        args:
            data (GameData): The game data.
        Returns:
            The auto-generated id of the new game
        """
        query = """
            INSERT INTO Game(GameName, GenreID, Developer, ReleaseDate, Cost)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (data.game_name, data.genre_id, data.developer, data.release_date, data.cost)
        return self.database_connection.create(query, values)
    
    def update(self, id_: int, data: GameData):
        """This method updates the game data in the database.
        args:
            id (int): The id of the game to be updated.
            data (GameData): The game data.
        """
        query="""
            UPDATE Game
            SET GameName = %s, GenreID = %s, Developer = %s, ReleaseDate = %s, Cost = %s
            WHERE Id = %s;
            """
        values = (data.game_name, data.genre_id, data.developer, data.release_date, data.cost, id_)
        self.database_connection.update(query, values)
    
    def delete(self, id_: int):
        """This method deletes the game from the database.
        args:
            id (int): The id of the game to be deleted.
        """
        query = """DELETE FROM Game 
                WHERE Id = %s;
                """
        values = (id_,)
        self.database_connection.delete(query, values)
    
    def get_by_id(self, id_: int) -> GameData:
        """This method gets a game from the repository based on the id.
        args:
            id (int): The id of the game to get.
        Returns:
            The game data.
        """
        query = """
            SELECT * FROM Game
            WHERE Id = %s;
            """
        values = (id_,)
        results = self.database_connection.get_one(query, values)
        game = {
            'game_id': results.get('Id', None),
            'game_name': results.get('GameName', None),
            'genre_id': results.get('GenreID', None),
            'developer': results.get('Developer', None),
            'release_date': results.get('ReleaseDate', None),
            'cost': results.get('Cost', None)
        }
        
        if not self.database_connection.get_one(query, values):
            return 'Game not found'
        return game
    
    def get_all(self) -> List[GameData]:
        """This method gets all the games data.
        Returns:
            A list of game data.
        """
        query = """
            SELECT * 
            FROM Game;
            """
        items = self.database_connection.get_many(query)
        results = [
                {
                    'game_id': row[0],
                    'game_name': row[1],
                    'genre_id': row[2],
                    'developer': row[3],
                    'release_date': row[4],
                    'cost': row[5]
                }
                for row in items
            ]
        return results

    def get_by_name(self, name: str):
        """This method gets a game from the repository based on the name.
        args:
            name (str): The name of the game to get.
        Returns:
            The game data.
        """
        query = """
            SELECT * FROM Game
            WHERE GameName LIKE %s;
            """
        values = (f"%{name}%",)
        items = self.database_connection.get_many(query, values)
        results = [
                {
                    'game_id': row[0],
                    'game_name': row[1],
                    'genre_id': row[2],
                    'developer': row[3],
                    'release_date': row[4],
                    'cost': row[5]
                }
                for row in items
            ]
        return results
    
    def get_by_genre(self, genre_id: int):
        """This method gets a list of games from the repository based on the genre.
        args:
            genre_id (int): The id of the genre.
        Returns:
            The game data.
        """
        query = f"""
            SELECT Game.Id, GameName, GenreID, Developer, ReleaseDate, Cost FROM Game
            JOIN Genre ON Game.GenreID = Genre.ID
            WHERE GenreID = {genre_id};
            """
        items = self.database_connection.get_many(query)
        results = [
                {
                    'game_id': row[0],
                    'game_name': row[1],
                    'genre_id': row[2],
                    'developer': row[3],
                    'release_date': row[4],
                    'cost': row[5]
                }
                for row in items
            ]
        return results   
    def get_by_dev(self, dev_id: str):
        """This method gets a game from the repository based on the dev.
        args:
            dev_id (int): The id of the dev.
        Returns:
            The game data.
        """
        query = """
            SELECT * FROM Game
            WHERE Developer = '{}';
            """.format(dev_id)
        items = self.database_connection.get_many(query)
        results = [
                {
                    'game_id': row[0],
                    'game_name': row[1],
                    'genre_id': row[2],
                    'developer': row[3],
                    'release_date': row[4],
                    'cost': row[5]
                }
                for row in items
            ]
        return results
    def get_genres(self):
        """This method gets all the genres.
        Returns:
            The genres data.
        """
        query = """
            SELECT * FROM Genre;
            """
        items = self.database_connection.get_many(query)
        results = [
                {
                    'genre_id': row[0],
                    'genre_name': row[1]
                }
                for row in items
            ]
        return results