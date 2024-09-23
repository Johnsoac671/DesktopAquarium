from webcolors import name_to_rgb

class Tile:
    def __init__(self):
        self.elements = []
        
    
    def get_top_element(self):
        pass
            
            

class Element:
    def __init__(self, name, color, symbol, is_alive):
        self.name = name
        self.color = color
        self.symbol = symbol
        self.is_alive = is_alive



class Water(Element):
    def __init__(self):
        super().__init__(name="water", color=name_to_rgb("cyan"), symbol="~", is_alive=False)



class Sand(Element):
    def __init__(self):
        super().__init__(name="sand", color=name_to_rgb("yellow"), symbol="*", is_alive=False)



class Aquarium:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[Water() for _ in range(self.width)] for _ in range(self.height)]
        self.add_substraite(3)
        
    
    def add_substraite(self, height):
        for x in range(height):
            self.grid[-x-1] = [Sand() for _ in range(self.width)]
        
    def get_grid(self):
        return list(map(lambda y: list(map(lambda x: (x.color, x.symbol), y)), self.grid))
        

