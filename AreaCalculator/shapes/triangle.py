import math
from shape import Shape

class Triangle(Shape):
    def __init__(self, side_a,side_b,side_c):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s=self.get_perimeter()/2
        return math.sqrt(s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c))

    def get_perimeter(self):
        return self.side_a+self.side_b+self.side_c
