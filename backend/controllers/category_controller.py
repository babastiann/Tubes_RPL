from dao.category_dao import CategoryDAO

class CategoryController:
    def __init__(self):
        self.category_dao = CategoryDAO()

    def list_categories(self):
        return self.category_dao.get_all_categories()

    def create_category(self, name):
        self.category_dao.add_category(name)

    def remove_category(self, category_id):
        self.category_dao.delete_category(category_id)
