"""
    Chain of responsability
    Its helps buildig a chain of objects, Request enters from one end and keeps
    going from object to object till it finds the object that can handle the request
"""
# from abc import ABC, abstractmethod

class Account:
    
    def __init__(self, balance) -> None:
        self.successor = None
        self.balance = balance
    
    def set_next(self, next_account):
        self.successor = next_account
    
    def can_pay(self,amount)-> bool:
        return self.balance >= amount
    
    def pay(self, amount_to_pay):
        
        if(self.can_pay(amount_to_pay)):
            print("Paying ",amount_to_pay, "from", self.__class__.__name__)
        elif(self.successor):
            print("Cannot pay using this account", "using",self.successor.__class__.__name__,"instead")
            self.successor.pay(amount_to_pay)
        else:
            raise Exception("No account to pay from")

class Bank(Account):
    
    def __init__(self, balance) -> None:
        self.balance = balance
        super().__init__(balance)

class Paypal(Account):
    
    def __init__(self, balance) -> None:
        self.balance = balance
        super().__init__(balance)

class Bitcoin(Account):
    
    def __init__(self, balance) -> None:
        self.balance = balance
        super().__init__(balance)

if __name__ == "__main__":
    bank = Bank(100)
    paypal = Paypal(200)
    bitcoin = Bitcoin(300)
    
    bank.set_next(paypal)
    paypal.set_next(bitcoin)
    
    bank.pay(250)
        
        