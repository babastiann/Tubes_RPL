from dao.base_dao import BaseDAO

class CategoryDAO(BaseDAO):
    def get_category(self, category_id):
        query = "SELECT * FROM categories WHERE id = %s"
        return self.fetch_one(query, (category_id,))

    def add_category(self, name):
        query = "INSERT INTO categories (name) VALUES (%s)"
        self.execute_query(query, (name,))

    def get_all_categories(self):
        query = "SELECT * FROM categories"
        return self.fetch_all(query)