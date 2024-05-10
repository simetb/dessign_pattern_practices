"""
    Factory Method
    It provides a way to delegate the instantiation 
    logic to child classes.
"""
from abc import ABC, abstractmethod

class Interviewer(ABC):
    @abstractmethod
    def ask_question(self):
        pass
    
class Developer(Interviewer):
    def ask_question(self):
        print("Asking about design patterns")

class CommunityExecutive(Interviewer):
    def ask_question(self):
        print("Asking about community building")
        

class HiringManager():
    @abstractmethod
    def make_interviewer(self) -> Interviewer:
        pass
    
    def take_interview(self):
        interviewer = self.make_interviewer();
        interviewer.ask_question()

class DevelopmentManager(HiringManager):
    
    def make_interviewer(self) -> Interviewer:
        return Developer()
    
class MarketingManager(HiringManager):
    def make_interviewer(self) -> Interviewer:
        return CommunityExecutive()

if __name__ == "__main__":
    devManager = DevelopmentManager()
    devManager.take_interview()
    
    marketingManager = MarketingManager()
    marketingManager.take_interview()
