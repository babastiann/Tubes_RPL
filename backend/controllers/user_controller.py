from dao.user_dao import UserDAO

class UserController:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, name, username, password, user_level, image, status):
        self.user_dao.add_user(name, username, password, user_level, image, status)

    def get_all_users(self):
        return self.user_dao.get_all_users()