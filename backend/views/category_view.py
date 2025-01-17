class CategoryView:
    def display_categories(self, categories):
        for category in categories:
            print(f"Category ID: {category['id']}, Name: {category['name']}")

    def display_message(self, message):
        print(message)