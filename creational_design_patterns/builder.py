"""
    Builder
    Allows you to create different flavors of an object while avoiding constructor pollution,
    Useful when there could be several flavors of an object. Or when there are a lot of steps involved 
    in creation of an object
"""

class Burguer:
    
    def __init__(self, builder) -> None:
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.lettuce = builder.lettuce
        self.tomato = builder.tomato
        
    def __str__(self) -> str:
        description = "Burguer: " + self.size
        if self.cheese:
            description += " cheese"
        if self.pepperoni:
            description += " pepperoni"
        if self.lettuce:
            description += " lettuce"
        if self.tomato:
            description += " tomato"
        return description
    
class BurguerBuilder:
    
    def __init__(self, size) -> None:
        self.size= size
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False
    
    def add_cheese(self) -> 'BurguerBuilder':
        self.cheese = True
        return self
    
    def add_pepperoni(self) -> 'BurguerBuilder':
        self.pepperoni = True
        return self
    
    def add_lettuce(self) -> 'BurguerBuilder':
        self.lettuce = True
        return self
    
    def add_tomato(self) -> 'BurguerBuilder':
        self.tomato = True
        return self
    
    def build(self) -> Burguer:
        return Burguer(self)

if __name__ == "__main__":
    burguer = (BurguerBuilder(size="medium")
               .add_cheese()
               .add_pepperoni()
               .add_lettuce()
               .add_tomato()
               .build())

    print(burguer)