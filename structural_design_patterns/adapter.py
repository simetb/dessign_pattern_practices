"""
    Adapter
    Adapter pattern lets you wrap an otherwise incompatible
    object in an adapter to make it compatible with another class
"""
from abc import ABC, abstractmethod

# Basic Structure
class Lion(ABC):
    @abstractmethod
    def roar(self) -> str:
        pass
    
class AfricanLion(Lion):
    def roar(self):
        return "Roar!"
    
class AsianLion(Lion):
    def roar(self):
        return "Roar!"
    
class Hunter:
    def hunt(self, lion : Lion):
        return lion.roar()

# Adapter Structure (Things that need to be added)
class WildDog:
    def bark(self):
        return "Bark!"
    
# Adapter
class WildDogAdapter(Lion):
    
    def __init__(self, dog : WildDog) -> None:
        self.dog = dog
    
    def roar(self) -> str:
        return self.dog.bark()
    
# Usage
if __name__ == "__main__":
    wildDog = WildDog()
    wildDogAdapter = WildDogAdapter(wildDog)
    
    hunter = Hunter()
    print(hunter.hunt(wildDogAdapter))
    

 