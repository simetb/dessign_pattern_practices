"""
    Prototype
    Create an object based on an existing object through cloning.
"""
import copy

class Sheep:
    
    def __init__(self, name, category = 'Mountain Sheep'):
        self.name = name
        self.category = category
        
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_category(self, category):
        self.category = category
        
    def get_category(self):
        return self.category
    

if __name__ == "__main__":
    original = Sheep('Fred')
    print(original.get_name())
    print(original.get_category())
    
    clone = copy.deepcopy(original)
    clone.set_name('Barney')
    print(clone.get_name())
    print(clone.get_category())
    
    
    
    