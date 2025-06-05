class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        if amount < 10:
            order_price = self.price * amount * 1
        elif amount >= 10 and amount <= 99:
            order_price = self.price * amount * 0.90

        elif amount >= 100:
            order_price = self.price * amount * 0.80

        return order_price

    def make_purchase(self, amount):
        if amount > self.amount:
            print("amaount is over the limit")
        else:
            self.amount -= amount


if __name__ == "__main__":
    pass
