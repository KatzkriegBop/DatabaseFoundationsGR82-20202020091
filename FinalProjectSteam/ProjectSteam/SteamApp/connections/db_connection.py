
"""This module is responsible for connecting to the MySQL database. 
It contains a class that handles the connection to the database, 
it also has the methods such as:
    - create: to add data to the database.
    - update: to update data in the database.
    - delete: to delete data from the database.
    - disconnect: to disconnect
    - connect: to connect 
"""

from typing import List
import mysql.connector
from mysql.connector import Error


class MySQLDatabaseConnection():
    """This class connects to the MySQL database."""

    def __init__(self):
        self._dbname = "steamproject"
        self._duser = "jpborjae1337"
        self._dpass = "katz12345"
        self._dhost = "mysql-db"
        self._dport = 3306
        self.connection = None
    
    
    def connect(self):
        """This method connects to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                database=self._dbname,
                user=self._duser,
                password=self._dpass,
                host=self._dhost,
                port=self._dport,
                auth_plugin='mysql_native_password',
            )
        except Error as e:
            print(f"MySQL Connection Error: {e}")

    def disconnect(self):
        """This method disconnects from the actual connection of the MySQL database."""
        if self.connection:
            self.connection.close()

    """def list_schemas(self):
        schemas = None
        try:
            query = "SHOW DATABASES;"
            cursor = self.connection.cursor()
            cursor.execute(query)
            schemas_db = cursor.fetchall()
            cursor.close()
            schemas = schemas_db
        except Error as e:
            print(f"MySQL Execution Error: {e}")

        return schemas
    """

    def create(self, query: str, values: tuple) -> int:
        """This method creates a new record in the database.
        Returns the id of the new record.
        args:
            query: str -> The query to execute.
            values: tuple -> The values to insert.
        """
        id_ = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            id_ = cursor.lastrowid
            cursor.close()
        except Error as e:
            print(f"MySQL Add Data Error: {e}")

        return id_

    def update(self, query: str, values: tuple):
        """This method connects to the MySQL database.
        args:
            query: str -> The query to execute.
            values: tuple -> The values to update.
        """
        try:
            print(query, values)
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"MySQL Update Data Error: {e}")

    def delete(self, query: str, item_id: tuple):
        """This method deletes a record from the database.
        args:
            query: str -> The query to execute.
            item_id: int -> The id of the record to delete.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, item_id)
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"MySQL Delete Data Error: {e}")

    def get_one(self, query: str, values: tuple) -> dict:
        """This method retrieves a single record from the database.
        Returns the record as a dictionary.
        args:
            query: str -> The query to execute.
            values: tuple -> The values to query.
        """
        item = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            item = cursor.fetchone()
            if item is not None:
                columns = [desc[0] for desc in cursor.description]
                item = dict(zip(columns, item)) 
            cursor.close()
        except Error as e:
            print(f"MySQL Get Data Error: {e}")
        return item if item is not None else {}

    def get_many(self, query: str, values: tuple = ()) -> List[dict]:
        """This method retrieves all records from the database.
        Returns the records as a list of dictionaries.
        args:
            query: str -> The query to execute.
            values: tuple -> The values to query.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            items = cursor.fetchall()
            cursor.close()
        except Error as e:  
            print(f"MySQL Get Data Error: {e}")

        return items
