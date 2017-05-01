"""
Modify the PredatoryCreditCard class from Section 2.4.1 so that a cus- tomer is assigned a minimum monthly payment, as a percentage of the balance, and so that a late fee is assessed if the customer does not subse- quently pay that minimum amount before the next monthly cycle
"""

class CreditCard:
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
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr, min_pay_percent):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._min_payment = min_pay_percent
        self._late_fee = 5
        self._peak_balance = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        if self._balance > self._peak_balance:
            self._peak_balance = self._balance
        return success

    def make_payment(self, amount):
        super().make_payment(amount)
        self._tt_payment += amount

    def process_month(self):
        if self._balance > 0:
            month_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
            if self._tt_payment < self._peak_balance * self._min_payment:
                self._balance += self._late_fee
        self._tt_payment = 0
        self._peak_balance = 0
