from dao.base_dao import BaseDAO

class SaleDAO(BaseDAO):
    def add_sale(self, product_id, qty, price, date):
        query = "INSERT INTO sales (product_id, qty, price, date) VALUES (%s, %s, %s, %s)"
        self.execute_query(query, (product_id, qty, price, date))

    def get_all_sales(self):
        query = "SELECT * FROM sales"
        return self.fetch_all(query)

    def update_sale(self, sale_id, product_id, qty, price, date):
        query = "UPDATE sales SET product_id = %s, qty = %s, price = %s, date = %s WHERE id = %s"
        self.execute_query(query, (product_id, qty, price, date, sale_id))

    def remove_sale(self, sale_id):
        query = "DELETE FROM sales WHERE id = %s"
        self.execute_query(query, (sale_id,))