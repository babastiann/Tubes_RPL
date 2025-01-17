from config import get_connection
import mysql.connector
import logging

class BaseDAO:
    def __init__(self):
        try:
            self.connection = get_connection()
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            logging.error(f"Database connection error: {err}")
            raise

    def execute_query(self, query, params=None):
        """
        Execute a query that modifies data (INSERT, UPDATE, DELETE).
        """
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except mysql.connector.Error as err:
            logging.error(f"Query execution error: {err}")
            self.connection.rollback()
            raise

    def fetch_all(self, query, params=None):
        """
        Execute a query and fetch all results.
        """
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            logging.error(f"Fetch all error: {err}")
            raise

    def fetch_one(self, query, params=None):
        """
        Execute a query and fetch one result.
        """
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            logging.error(f"Fetch one error: {err}")
            raise

    def __enter__(self):
        """
        Allow the DAO to be used as a context manager.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Clean up resources when context exits.
        """
        self.__del__()

    def __del__(self):
        """
        Clean up the database connection and cursor.
        """
        try:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()
        except mysql.connector.Error as err:
            logging.error(f"Error closing resources: {err}")
