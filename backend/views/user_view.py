class UserView:
    def display_users(self, users):
        for user in users:
            print(f"User ID: {user['id']}, Name: {user['name']}, Username: {user['username']}, User Level: {user['user_level']}, Status: {user['status']}")

    def display_message(self, message):
        print(message)