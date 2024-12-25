#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}.")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}.")

class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.process_payment(amount)

class PaymentMethod:
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}.")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}.")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.process_payment(amount)

payment_method = CreditCardPayment()
payment_processor = PaymentProcessor(payment_method)
payment_processor.process(150)

payment_method = PayPalPayment()
payment_processor = PaymentProcessor(payment_method)
payment_processor.process(250)

