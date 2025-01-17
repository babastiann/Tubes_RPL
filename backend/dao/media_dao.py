from dao.base_dao import BaseDAO

class MediaDAO(BaseDAO):
    def get_media(self, media_id):
        query = "SELECT * FROM media WHERE id = %s"
        return self.fetch_one(query, (media_id,))

    def add_media(self, file_name, file_type):
        query = "INSERT INTO media (file_name, file_type) VALUES (%s, %s)"
        self.execute_query(query, (file_name, file_type))

    def get_all_media(self):
        query = "SELECT * FROM media"
        return self.fetch_all(query)