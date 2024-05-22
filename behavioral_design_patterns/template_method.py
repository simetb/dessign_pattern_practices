"""
    Template Method
    Template Method defines the skeleton of a how a certain algorithm could be perfomed,
    but defers the implementation of those steps to the children classes.
"""
from abc import ABC, abstractmethod

class Builder(ABC):

    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()
    
    @abstractmethod
    def test(self):pass
    
    @abstractmethod
    def lint(self):pass
    
    @abstractmethod
    def assemble(self):pass
    
    @abstractmethod
    def deploy(self):pass
    

class AndroidBuilder(Builder):
    def test(self):
        print("Running Android tests")
    
    def lint(self):
        print("Running Android lint")
    
    def assemble(self):
        print("Assembling Android app")
    
    def deploy(self):
        print("Deploying Android app")

class IosBuilder(Builder):
    def test(self):
        print("Running iOS tests")
    
    def lint(self):
        print("Running iOS lint")
    
    def assemble(self):
        print("Assembling iOS app")
    
    def deploy(self):
        print("Deploying iOS app")
        

if __name__ == "__main__":
    android_builder = AndroidBuilder()
    android_builder.build()
    
    print("")

    ios_builder = IosBuilder()
    ios_builder.build()