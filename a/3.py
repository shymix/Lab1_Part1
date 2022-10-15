class Product:
    def __init__(self, descr, price: float = 1):
        self.__descr = descr
        if not isinstance(price, float):
            raise TypeError
        self.__price = price

    def price(self):
        return self.__price

class Person:
    def __init__(self, name):
        self.__name = name

    def name(self):
        return self.__name

class Order:
    def __init__(self, person: Person):
        self.customer = person
        self.order = {}

    def add_product(self, product: Product, quantity: int = 1):
        T = False
        for k, v in self.order.items():
            if k == product:
                self.order[k] = self.order[k]+quantity
                T = True
        if not T:
            self.order[product] = quantity

    def total(self):
        total = 0
        for k, v in self.order.items():
            total = total + k.price() * v
        return total

tomato = Product("Big red vegetable", 10.0)
cheese = Product("Yellow thing made from milk", 15.5)
cucumber = Product("Long green vegetable", 8.25)
meat = Product("tasty part of dead animal", 25.3)

John = Person('John')

receipt = Order(John)
receipt.add_product(tomato, 5)
receipt.add_product(cheese, 8)
receipt.add_product(meat, 3)
print(receipt.customer.name(), "'s total receipt = ", receipt.total())
receipt.add_product(tomato, 5)
print(receipt.customer.name(), "'s total receipt = ", receipt.total())
