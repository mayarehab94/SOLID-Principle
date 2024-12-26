#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# this code violate the SOLID principles
class PaymentMethod:
    def CreditCardPayment(self, amount):
        print(f"Processing credit card payment of {amount}.")
        
    def PayPalPayment(self, amount):
        print(f"Processing PayPal payment of {amount}.")
        

class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        
    def process_CreditCard(self, amount):
        self.payment_method.CreditCardPayment(amount)

    def process_PayPal(self, amount):
        self.payment_method.PayPalPayment(amount)

#This code dosenot violate the SOLID princible
from abc import ABC , abstractmethod 
class PaymentMethod:
    @abstractmethod
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


