"""
    State
    It lets you change the behavior of a class when the state of an object changes.
"""
from abc import ABC, abstractmethod

class PhoneState(ABC):
    @abstractmethod
    def pick_up(self): pass
    
    @abstractmethod
    def hang_up(self): pass
    
    @abstractmethod
    def dial(self): pass
    

class PhoneStateIdle(PhoneState):
    def pick_up(self) -> PhoneState: 
        return PhoneStatePickedUp()
    
    def hang_up(self) -> PhoneState:
        raise Exception("Already idle")
    
    def dial(self) -> PhoneState:
        raise Exception("Can't dial when idle")
    
class PhoneStatePickedUp(PhoneState):
    def pick_up(self) -> PhoneState: 
        raise Exception("Already picked up")
    
    def hang_up(self)-> PhoneState:
        return PhoneStateIdle()
    
    def dial(self) -> PhoneState:
        return PhoneStateCalling()

class PhoneStateCalling(PhoneState):
    def pick_up(self) -> PhoneState: 
        raise Exception("Already picked up")
    
    def hang_up(self) -> PhoneState: 
        return PhoneStateIdle()
    
    def dial(self) -> PhoneState:
        raise Exception("already dialing")

class Phone:
    
    def __init__(self) -> None:
        self.sate = PhoneStateIdle()
    
    def pick_up(self):
        self.sate = self.sate.pick_up()
        
    def hang_up(self):
        self.sate = self.sate.hang_up()
        
    def dial(self):
        self.sate = self.sate.dial()

if __name__ == "__main__":
   phone = Phone()
   phone.pick_up()
   phone.dial() 
    
        
 