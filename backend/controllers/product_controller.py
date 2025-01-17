from dao.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self.product_dao = ProductDAO()

    def list_products(self):
        return self.product_dao.get_all_products()

    def create_product(self, name, quantity, buy_price, sale_price, category_id, media_id, date):
        self.product_dao.add_product(name, quantity, buy_price, sale_price, category_id, media_id, date)

    def update_product(self, product_id, name, quantity, buy_price, sale_price, category_id, media_id, date):
        self.product_dao.update_product(product_id, name, quantity, buy_price, sale_price, category_id, media_id, date)

    def remove_product(self, product_id):
        self.product_dao.delete_product(product_id)
