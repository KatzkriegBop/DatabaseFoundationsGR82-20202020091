
from typing import List
from DataAccessObjects.user_data import UserData
from connections import db_connection
from DataAccessObjects.friend_data import FriendData

class FriendsCRUD:
    """This class is responsible for performing CRUD operations on the friends table.
    
    Attributes:
        database_connection (db_connection): The database connection

    methods:
        create: Creates a new friend in the database.
        delete: Deletes the friend from the database.
        is_friend: Checks if the user is already friends with the friend.
        get_all: Gets all the friends data.
        get_by_user_id: Gets a friend from the repository based on the user id.
        get_by_friend_id: Gets a friend from the repository based on the friend id.
        get_friends_by_user_id: Gets all the friends of a user based on the user id.
    """
    def __init__(self, db_connection: db_connection):
        self.database_connection = db_connection
        self.database_connection.connect()
    
    def create(self, data: FriendData) -> int:
        """This method creates a new friend in the database.
        args:
            data (FriendData): The friend data.
        Returns:
            The auto-generated id of the new friend
        """
        query = """
            INSERT INTO Friends(UserID, UserFriendID)
            VALUES (%s, %s)
        """
        values = (data.user_id, data.friend_id)
        return self.database_connection.create(query, values)
    
    def delete(self, user_id: int, friend_id: int):
        """This method deletes the friend from the database.
        args:
            user_id (int): The user id to be deleted.
            friend_id (int): The friend id of the friend to be deleted.
        """
        query = """DELETE FROM Friends 
            WHERE (UserID = %s AND UserFriendID = %s) 
            OR (UserID = %s AND UserFriendID = %s)
            """
        values = (user_id, friend_id, friend_id, user_id)
        self.database_connection.delete(query, values)
    
    def is_friend(self, user_id: int, friend_id: int) -> bool:
        """This method checks if the user is already friends with the friend.
        args:
            user_id (int): The user id.
            friend_id (int): The friend id.
        Returns:
            True if the user is already friends with the friend, False otherwise.
        """
        query = """SELECT COUNT(*) FROM Friends 
                WHERE (UserID = %s AND UserFriendID = %s) 
                OR (UserID = %s AND UserFriendID = %s)
                """
        values = (user_id, friend_id,friend_id,user_id)
        result = self.database_connection.get_one(query, values)
        if result and result['COUNT(*)'] > 0:
                    return True
        return False

    def get_all(self) -> List[FriendData]:
        """This method gets all the friends data.
        Returns:
            A list of all the friends data.
        """
        query = """SELECT * FROM Friends"""
        items = self.database_connection.get_many(query)
        results = [
                {
                    'user_id': row[0],
                    'friend_id': row[1]
                }
                for row in items
            ]
        return results
    def get_by_user_id(self, user_id: int) -> List[UserData]:
        """This method gets a friend from the repository based on the user id.
        args:
            user_id (int): The user id of the friend.
        Returns:
            The friend data.
        """
        query = """SELECT * 
                FROM Friends 
                JOIN User ON User.SteamID = 
                    CASE
                        WHEN Friends.UserID = %s THEN Friends.UserFriendID
                        ELSE Friends.UserID
                    END
                WHERE %s IN (Friends.UserID, Friends.UserFriendID)
                """
        values = (user_id, user_id)
        items = self.database_connection.get_many(query, values)
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