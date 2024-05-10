"""
    Simple facroty
    Simple factory simply generates an instance for client
    witouth exposing any instantation logic to the client
"""
from abc import ABC, abstractmethod

class Door(ABC):
    
    @abstractmethod
    def get_width(self) -> float:
        pass
    
    @abstractmethod
    def get_height(self) -> float:
        pass
    
class WoodenDoor(Door):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        
    def get_width(self) -> float:
        # Some Complex logic
        return self.width
    
    def get_height(self) -> float:
        # Some Complex logic
        return self.height
    
class DoorFactory():
    
    @staticmethod
    def make_door(width: float, height: float):
        return WoodenDoor(width, height)
    

if __name__ == "__main__":
    # Make me a door 100x200
    print("First Door")
    door = DoorFactory.make_door(100, 200)
    print("Door width: ", door.get_width())
    print("Door height: ", door.get_height())

    # Space
    print()
        
    # Make me a door 50x100
    print("Second Door")
    door = DoorFactory.make_door(50, 100)
    print("Door width: ", door.get_width())
    print("Door height: ", door.get_height())
    
    
    

    
    