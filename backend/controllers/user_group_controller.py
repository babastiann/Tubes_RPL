from dao.user_group_dao import UserGroupDAO

class UserGroupController:
    def __init__(self):
        self.user_group_dao = UserGroupDAO()

    def create_user_group(self, group_name, group_level, group_status):
        self.user_group_dao.add_user_group(group_name, group_level, group_status)

    def get_all_user_groups(self):
        return self.user_group_dao.get_all_user_groups()