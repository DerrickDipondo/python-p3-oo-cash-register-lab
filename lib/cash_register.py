#!/usr/bin/env python3
import io
import sys

class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.discount = discount
        self.last_transaction_amount = 0
        self.last_transaction_quantity = 0 

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction_amount = price * quantity
        self.last_transaction_quantity = quantity 
        
    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        if self.total < 0: 
            self.total = 0
        
        self.last_transaction_amount = 0
        self.last_transaction_quantity = 0



