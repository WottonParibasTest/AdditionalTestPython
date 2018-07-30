class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class ProductInstance:
    def __init__(self, product, count):
        self.product = product
        self.count = count

    def __str__(self):
        return "{} {}".format(self.product.name, self.count)

