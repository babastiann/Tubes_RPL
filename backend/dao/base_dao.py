from config import get_connection

class BaseDAO:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
