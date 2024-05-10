"""
    Abstract Factory
    A factory of factories; a factory that groups the individual but related/dependent factories
    together without specifying their classes.
"""

from abc import ABC, abstractmethod

class Door(ABC):
    @abstractmethod
    def getDescription(self) -> None: pass
    
class WoodenDoor(Door):
    def getDescription(self)-> None:
        print("I am a wooden door")

class IronDoor(Door):
    def getDescription(self) -> None:
        print("I am a tron door")

class DoorFiltingExpert(ABC):
    @abstractmethod
    def getDescription(self) -> None: pass

class Welder(DoorFiltingExpert):
    def getDescription(self) -> None:
        print("I can only fit iron dors")

class Carpenter(DoorFiltingExpert):
    def getDescription(self) -> None:
        print("I can only fit wooden dors")
        
class DoorFactory(ABC):
    @abstractmethod
    def makeDoor(self) -> Door: pass
    
    @abstractmethod
    def makeFiltingExpert(self) -> DoorFiltingExpert: pass

class WoodenDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        return WoodenDoor()
    
    def makeFiltingExpert(self) -> DoorFiltingExpert:
        return Carpenter()

class IronDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        return IronDoor()
    
    def makeFiltingExpert(self) -> DoorFiltingExpert:
        return Welder()
    
if __name__ == "__main__":
    # Info wood factory
    woodenFactory = WoodenDoorFactory()
    door = woodenFactory.makeDoor()
    expert = woodenFactory.makeFiltingExpert()
    
    door.getDescription()
    expert.getDescription()
    
    #Info iron factory
    ironFactory = IronDoorFactory()
    door = ironFactory.makeDoor()
    expert = ironFactory.makeFiltingExpert()
    
    door.getDescription()
    expert.getDescription()
    