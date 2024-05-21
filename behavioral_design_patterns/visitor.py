"""
Visitor
Visitor pattern lets you add further operations to objects without 
having to modify them.
"""
from abc import ABC, abstractmethod

# Visitees
class Animal(ABC):
    @abstractmethod
    def accept(self, visitor): pass

# Visitor
class AnimalOperations(ABC):
    @abstractmethod
    def visit_monkey(self, monkey): pass
        
    @abstractmethod
    def visit_lion(self, lion): pass
        
    @abstractmethod
    def visit_dolphin(self, dolphin): pass

class Monkey(Animal):
    def shout(self):
        print("Ooh ooh ooh")
    
    def accept(self, operation: AnimalOperations):
        operation.visit_monkey(self)

class Lion(Animal):
    def roar(self):
        print("Roar roar roar")
        
    def accept(self, operation: AnimalOperations):
        operation.visit_lion(self)
        
class Dolphin(Animal):
    def speak(self):
        print("tuut tuttu tuttti")
        
    def accept(self, operation: AnimalOperations):
        operation.visit_dolphin(self)


# Implementing the Visitor
class Speak(AnimalOperations):
    
    def visit_monkey(self, monkey: Monkey):
        monkey.shout()
    
    def visit_lion(self, lion: Lion):
        lion.roar()
    
    def visit_dolphin(self, dolphin: Dolphin):
        dolphin.speak()
        
class Jump(AnimalOperations):
    def visit_monkey(self, monkey: Monkey):
        print("Monkey is jumping 10ft")
        
    def visit_lion(self, lion: Lion):
        print("Lion is jumping 5ft")
        
    def visit_dolphin(self, dolphin: Dolphin):
        print("WTF is dolphin doing here")

# And then we can use it as
if __name__ == "__main__":
    monkey = Monkey()
    lion = Lion()
    dolphin = Dolphin()
    
    speak = Speak()
    jump = Jump()
    
    monkey.accept(speak)
    monkey.accept(jump)
    
    lion.accept(speak)
    lion.accept(jump)
    
    dolphin.accept(speak)
    dolphin.accept(jump)
