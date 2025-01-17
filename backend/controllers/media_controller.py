from dao.media_dao import MediaDAO

class MediaController:
    def __init__(self):
        self.media_dao = MediaDAO()

    def create_media(self, file_name, file_type):
        self.media_dao.add_media(file_name, file_type)

    def get_all_media(self):
        return self.media_dao.get_all_media()