from dao.product_dao import ProductDAO
from dao.sale_dao import SaleDAO

class SaleController:
    def __init__(self, sale_dao):
        self.sale_dao = sale_dao
        self.product_dao = ProductDAO()

    def create_sale(self, product_id, qty, price, date):
        # Check if product exists
        product = self.product_dao.get_product(product_id)
        if not product:
            # Add product if it doesn't exist
            self.product_dao.add_product("Default Product Name", price)
            product_id = self.product_dao.get_product(product_id)['id']
        
        self.sale_dao.add_sale(product_id, qty, price, date)

    def get_all_sales(self):
        return self.sale_dao.get_all_sales()

    def update_sale(self, sale_id, product_id, qty, price, date):
        self.sale_dao.update_sale(sale_id, product_id, qty, price, date)

    def remove_sale(self, sale_id):
        self.sale_dao.remove_sale(sale_id)