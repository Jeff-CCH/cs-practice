"""
Use the techniques of Section 1.7 to revise the charge and make payment methods of the CreditCard class to ensure that the caller sends a number as a parameter.
"""

class CreditCard:
    """A consumer credit card. """

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if isinstance(price, int) is False:
            raise TypeError("price must be an integer")
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if isinstance(amount, int) is False:
            raise TypeError("price must be an integer")
        self._balance -= amount

def main():
    try:
        c = CreditCard("AC", "UK", "UK1", 1000)
        print c.charge(100)
        c.make_payment(20)
        print c.get_balance()
        c.charge('candy')
    except Exception, e:
        print e

if __name__ == '__main__':
    main()
