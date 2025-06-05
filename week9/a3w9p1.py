class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold_to = None
        self.sold = False

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        print(f'brand: {self.brand}')
        print(f'model: {self.model}')
        print(f'color: {self.color}')
        print(f'price: {self.price}:')
        if self.sold_to:
            print(f'sold to {self.sold_to.name}')
        else:
            print('not sold yet')


class Motorcycle:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold_to = None
        self.sold = False

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        print(f'brand: {self.brand}')
        print(f'model: {self.model}')
        print(f'color: {self.color}')
        print(f'price: {self.price}')
        if self.sold_to:
            print(f'sold to {self.sold_to.name}')
        else:
            print('not sold yet')


class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'name {self.name}')


customer1 = Customer('John Doe')
car1 = Car(f'BMW', 'M4', 'Black', 50.000)
motorcycle1 = Motorcycle(f"Kawasaki", "H2", "Green", 36.999)


if __name__ == "__main__":
    car1.sell(customer1)
    car1.print()
    motorcycle1.sell(customer1)
    motorcycle1.print()
