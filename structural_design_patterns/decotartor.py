"""
    Decorator
    Decorator pattern let you dynamically change the behavior of an object
    at run time by wrapping them in an object of a decorator class
"""
from abc import ABC, abstractmethod

class Coffe(ABC):
    @abstractmethod
    def getcost(self) -> int: pass

    @abstractmethod
    def getdescription(self) -> str: pass

class SimpleCoffe(Coffe):
    def getcost(self):
        return 10
    
    def getdescription(self):
        return "SImple coffe"



class SimpleCoffe(Coffe):
    def getcost(self):
        return 10
    
    def getdescription(self):
        return "SImple coffe"

class MilkCoffe(Coffe):

    def __init__(self,the_coffe : Coffe):
        self.coffe = the_coffe
        pass

    def getcost(self):
        return self.coffe.getcost() + 2
    
    def getdescription(self):
        return self.coffe.getdescription() + " Milk"

class WhipCoffe(Coffe):

    def __init__(self,the_coffe : Coffe):
        self.coffe = the_coffe
        pass

    def getcost(self):
        return self.coffe.getcost() + 5
    
    def getdescription(self):
        return self.coffe.getdescription() + " Whip"

class VanillaCoffe(Coffe):

    def __init__(self,the_coffe : Coffe):
        self.coffe = the_coffe
        pass

    def getcost(self):
        return self.coffe.getcost() + 3
    
    def getdescription(self):
        return self.coffe.getdescription() + " Vanilla"


if __name__ == "__main__":
    some_coffe = SimpleCoffe()
    print(some_coffe.getcost())
    print(some_coffe.getdescription())

    some_coffe = MilkCoffe(some_coffe)
    print(some_coffe.getcost())
    print(some_coffe.getdescription())

    some_coffe = WhipCoffe(some_coffe)    
    print(some_coffe.getcost())
    print(some_coffe.getdescription())

    some_coffe = VanillaCoffe(some_coffe)
    print(some_coffe.getcost())
    print(some_coffe.getdescription())
5