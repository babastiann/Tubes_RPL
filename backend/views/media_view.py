class MediaView:
    def display_media(self, media_list):
        for media in media_list:
            print(f"Media ID: {media['id']}, File Name: {media['file_name']}, File Type: {media['file_type']}")

    def display_message(self, message):
        print(message)