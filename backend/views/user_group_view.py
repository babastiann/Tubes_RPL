class UserGroupView:
    def display_user_groups(self, user_groups):
        for group in user_groups:
            print(f"Group ID: {group['id']}, Group Name: {group['group_name']}, Group Level: {group['group_level']}, Group Status: {group['group_status']}")

    def display_message(self, message):
        print(message)