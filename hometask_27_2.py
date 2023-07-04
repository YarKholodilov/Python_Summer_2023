class Item:
    def __init__(self, name, price, quantity):
        self.name = name.title()
        self.price = price
        self.quantity = quantity

    def __getattr__(self, total):
        self.total = (self.price * self.quantity)
        return self.total


d = Item('col', 4, 10)
print(d.name)
print(d.price)
print(d.quantity)
print(d.total)
