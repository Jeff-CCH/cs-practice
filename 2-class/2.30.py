"""
At the close of Section2.4.1,we suggest a model in which the CreditCard class supports a nonpublic method, set balance(b), that could be used by subclasses to affect a change to the balance, without directly accessing the balance data member. Implement such a model, revising both the CreditCard and PredatoryCreditCard classes accordingly
"""

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def _set_balance(self, val):
        self._balance = val

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
            self._set_balance(self._balance + price)
            return True

    def make_payment(self, amount):
        self._set_balance(self._balance - amount)

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr, min_pay_percent):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            super()._set_balance(self._balance + 5)
        return success

    def make_payment(self, amount):
        super().make_payment(amount)

    def process_month(self):
        if self._balance > 0:
            month_factor = pow(1 + self._apr, 1/12)
            super()._set_balance(self._balance * monthly_factor)
