"""
    Flyweight
    It is used to minimize memory usage or computational expenses by sharing as much as possible
    with similar objects
"""

class KarakTea:
    pass


class TeaMaker:
    
    def __init__(self):
        self.available_tea = {}
    
    def make(self, preference):
        if preference not in self.available_tea:
            self.available_tea[preference] = KarakTea()
        
        return self.available_tea[preference]
    

class TeaShop:
    
    def __init__(self, tea_maker: TeaMaker):
        self.tea_maker = tea_maker
        self.orders = {}
    
    def take_order(self, tea_type: str, table: int):
        self.orders[table] = self.tea_maker.make(tea_type)
    
    def serve(self):
        for table, tea in self.orders.items():
            print(f"Serving tea to table {table}")


if __name__ == "__main__":
    tea_maker = TeaMaker()
    shop = TeaShop(tea_maker)

    shop.take_order("less sugar", 1)
    shop.take_order("more milk", 2)
    shop.take_order("without sugar", 5)

    shop.serve()
