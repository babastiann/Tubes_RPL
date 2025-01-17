import bcrypt
from dao.base_dao import BaseDAO

class UserDAO(BaseDAO):
    def get_user(self, user_id):
        """
        Retrieve a user by their ID.
        """
        query = "SELECT * FROM users WHERE id = %s"
        return self.fetch_one(query, (user_id,))

    def get_user_by_username(self, username):
        """
        Retrieve a user by their username.
        """
        query = "SELECT * FROM users WHERE username = %s"
        user = self.fetch_one(query, (username,))
        if user:
            return {
                'id': user['id'],
                'username': user['username'],
                'password': user['password'],  # Hashed password
                'user_level': user['user_level'],
                'image': user['image'],
                'status': user['status']
            }
        return None

    def add_user(self, name, username, password, user_level, image=None, status='active'):
        """
        Add a new user with hashed password.
        """
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        query = """
        INSERT INTO users (name, username, password, user_level, image, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.execute_query(query, (name, username, hashed_password, user_level, image, status))

    def get_all_users(self):
        """
        Retrieve all users.
        """
        query = "SELECT * FROM users"
        users = self.fetch_all(query)
        return [
            {
                'id': user['id'],
                'username': user['username'],
                'user_level': user['user_level'],
                'image': user['image'],
                'status': user['status']
            }
            for user in users
        ]
