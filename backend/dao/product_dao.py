from dao.base_dao import BaseDAO
from models.product import Product

class ProductDAO(BaseDAO):
    def get_all_products(self):
        query = "SELECT * FROM products"
        result = self.execute_query(query)
        return [Product(**row) for row in result]

    def add_product(self, name, quantity, buy_price, sale_price, category_id, media_id, date):
        query = """
            INSERT INTO products (name, quantity, buy_price, sale_price, categorie_id, media_id, date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.execute_query(query, (name, quantity, buy_price, sale_price, category_id, media_id, date))
        self.commit()

    def update_product(self, product_id, name, quantity, buy_price, sale_price, category_id, media_id, date):
        query = """
            UPDATE products
            SET name = %s, quantity = %s, buy_price = %s, sale_price = %s, 
                categorie_id = %s, media_id = %s, date = %s
            WHERE id = %s
        """
        self.execute_query(query, (name, quantity, buy_price, sale_price, category_id, media_id, date, product_id))
        self.commit()

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE id = %s"
        self.execute_query(query, (product_id,))
        self.commit()
