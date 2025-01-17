from dao.base_dao import BaseDAO

class UserGroupDAO(BaseDAO):
    def get_user_group(self, group_id):
        query = "SELECT * FROM user_groups WHERE id = %s"
        return self.fetch_one(query, (group_id,))

    def add_user_group(self, group_name, group_level, group_status):
        query = "INSERT INTO user_groups (group_name, group_level, group_status) VALUES (%s, %s, %s)"
        self.execute_query(query, (group_name, group_level, group_status))

    def get_all_user_groups(self):
        query = "SELECT * FROM user_groups"
        return self.fetch_all(query)