from dao.base_dao import BaseDAO
from models.category import Category

class CategoryDAO(BaseDAO):
    def get_all_categories(self):
        query = "SELECT * FROM categories"
        result = self.execute_query(query)
        return [Category(**row) for row in result]

    def add_category(self, name):
        query = "INSERT INTO categories (name) VALUES (%s)"
        self.execute_query(query, (name,))
        self.commit()

    def delete_category(self, category_id):
        query = "DELETE FROM categories WHERE id = %s"
        self.execute_query(query, (category_id,))
        self.commit()
