import bcrypt
from config import get_connection

def update_passwords():
    connection = get_connection()
    cursor = connection.cursor()

    # Fetch all users
    cursor.execute("SELECT id, password FROM users")
    users = cursor.fetchall()

    for user in users:
        user_id = user[0]
        password = user[1]

        # Check if the password is already hashed
        if not password.startswith('$2b$'):
            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # Update the password in the database
            cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user_id))

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    update_passwords()