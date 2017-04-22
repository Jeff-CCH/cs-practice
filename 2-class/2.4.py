"""
Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the name of the flower, its num- ber of petals, and its price. Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type.
"""

class Flower():
    def __init__(self, name, num_petal, price):
        self.name = name
        self.num_petal = num_petal
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print self.name

    def set_num_petal(self, num_petal):
        self.num_petal = num_petal

    def get_num_petal(self):
        print self.num_petal

    def set_price(self, price):
        self.price = price

    def get_price(self):
        print self.price

def main():
    f1 = Flower('Rose', 3, 10.00)
    f1.get_name()
    f1.get_num_petal()
    f1.get_price()
    f1.set_num_petal(10)
    f1.get_num_petal()

    f2 = Flower('Tulip', 10, 25.00)
    f2.get_name()
    f2.get_num_petal()
    f2.get_price()
    f2.set_price(25.05)
    f2.get_price()

if __name__ == '__main__':
    main() 
