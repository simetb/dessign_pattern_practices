"""
    Command
    Allows you to encapsulate actions in objects. The key idea behind this pattern
    is to provide the means to decouple client from receiver.
"""
from abc import ABC, abstractmethod

# Receiver
class Bulb:
    def turn_on(self):
        print("Bulb has been lit")
    
    def turn_off(self):
        print("Darkness!")

class Command(ABC):
    @abstractmethod
    def execute(self): pass
    
    @abstractmethod
    def undo(self): pass
    
    @abstractmethod
    def redo(self): pass
    
class TurnOn (Command):
    def __init__(self, bulb):
        self.bulb = bulb
    
    def execute(self):
        self.bulb.turn_on()
    
    def undo(self):
        self.bulb.turn_off()
        
    def redo(self):
        self.execute()

class TurnOff (Command):
    def __init__(self, bulb):
        self.bulb = bulb
        
    def execute(self):
        self.bulb.turn_off()
    
    def undo(self):
        self.bulb.turn_on()
    
    def redo(self):
        self.execute()

# Invoker
class RemoteControl:
    def submit(self, command):
        command.execute()


if __name__ == "__main__":
    bulb = Bulb()
    
    turOn = TurnOn(bulb)
    turnOff = TurnOff(bulb)
    
    remote = RemoteControl()
    remote.submit(turOn)
    remote.submit(turnOff)
