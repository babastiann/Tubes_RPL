class ProductView:
    @staticmethod
    def display_products(products):
        print("Products:")
        for product in products:
            print(
                f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, "
                f"Buy Price: {product.buy_price}, Sale Price: {product.sale_price}, "
                f"Category ID: {product.category_id}, Media ID: {product.media_id}, Date: {product.date}"
            )

    @staticmethod
    def display_message(message):
        print(message)
