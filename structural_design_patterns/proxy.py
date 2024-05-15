"""
    Proxy
    Using the proxy pattern a class represents the funcitonality of another class
"""
from abc import ABC, abstractmethod


class Door(ABC):
    @abstractmethod
    def open(self): pass

    @abstractmethod
    def close(self): pass


class LabDoor(Door):

    def open(self):
        print("Opening lab door")
    
    def close(self):
        print("Closing the labd door")


class SecuredDoor(Door):

    def __init__(self, door: Door):
        self.door = door

    def authenticate(self,password):
        return password == "123"

    def open(self, password):
        if(self.authenticate(password)):
            self.door.open(self)
        else:
            print("Big no! it ain't be possible")
    
    def close(self):
        self.door.close(self)

if __name__ == "__main__":
    door = SecuredDoor(LabDoor)
    door.open("345678")

    door.open("123")
    door.close()
