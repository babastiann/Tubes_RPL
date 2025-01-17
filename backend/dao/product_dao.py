from dao.base_dao import BaseDAO

class ProductDAO(BaseDAO):
    def get_product(self, product_id):
        query = "SELECT * FROM products WHERE id = %s"
        return self.fetch_one(query, (product_id,))

    def add_product(self, name, price):
        query = "INSERT INTO products (name, price) VALUES (%s, %s)"
        self.execute_query(query, (name, price))