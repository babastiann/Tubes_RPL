class CategoryView:
    @staticmethod
    def display_categories(categories):
        print("Categories:")
        for category in categories:
            print(f"- {category.id}: {category.name}")

    @staticmethod
    def display_message(message):
        print(message)
