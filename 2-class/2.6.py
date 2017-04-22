"""
If the parameter to the make payment method of the CreditCard class were a negative number, that would have the effect of raising the balance on the account. Revise the implementation so that it raises a ValueError if a negative value is sent.
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
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if amount < 0:
            raise ValueError("payment cannot be a negative num")
        self._balance -= amount

def main():
    try:
        c = CreditCard("AC", "UK", "UK1", 1000)
        c.charge(100)
        print c.get_balance()
        c.make_payment(20)
        print c.get_balance()
        c.make_payment(-20)
    except Exception, e:
        print e

if __name__ == '__main__':
    main()
