from dao.category_dao import CategoryDAO

class CategoryController:
    def __init__(self):
        self.category_dao = CategoryDAO()

    def create_category(self, name):
        self.category_dao.add_category(name)

    def get_all_categories(self):
        return self.category_dao.get_all_categories()