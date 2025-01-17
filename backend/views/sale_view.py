class SaleView:
    def display_sales(self, sales):
        for sale in sales:
            print(f"Sale ID: {sale['id']}, Product ID: {sale['product_id']}, Quantity: {sale['qty']}, Price: {sale['price']}, Date: {sale['date']}")

    def display_message(self, message):
        print(message)