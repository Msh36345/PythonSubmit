import math
from shape import Shape

class Hexagon(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

    def get_perimeter(self):
        return 6 * self.side