class Product:
    id = 0
    title = ""
    category = ""
    stock = 0
    price = 0.0

    def __init__(self, id, title, category, stock, price):
        self.id = id
        self.title = title
        self.category = category
        self.stock = stock
        self.price = price

    def print(self):
        print(
            f"{str(self.id).rjust(10)} | {str(self.title).rjust(20)} | {str(self.category).rjust(20)} | {str(self.stock).rjust(20)} | ${'{:,.2f}'.format(self.price).rjust(20)}")
