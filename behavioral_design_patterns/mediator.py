"""
    Mediator
    Mediator pattern adds a third party object (called mediator) to control the interaction between two
    objects (called collegues) it helps reduce the coupling between the classes communicating with each other.
    Because now they don't need to have the knowledge of each other's implementation.
"""
from abc import ABC, abstractmethod
from datetime import datetime

class MediatorInterface(ABC):
    @abstractmethod
    def show_message(user, message:str):pass
    
# Mediator
class ChatRoom(MediatorInterface):
    def show_message(self, user, message: str):
        time = datetime.now()
        sender = user.get_name()
        print("[{}] {}: {}".format(time, sender, message))
        

class User:
    def __init__(self, name:str, chat_mediator : ChatRoom) -> None:
        self.name = name
        self.chat_mediator = chat_mediator
    
    def get_name(self):
        return self.name
    
    def send_message(self, message:str):
        self.chat_mediator.show_message(self, message)
        

if __name__ == "__main__":
    mediatpr = ChatRoom()
    john = User("John", mediatpr)
    jane = User("Jane", mediatpr)
    
    john.send_message("Hello Jane!")
    jane.send_message("Hi John!")