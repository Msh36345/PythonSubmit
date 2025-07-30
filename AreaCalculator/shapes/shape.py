from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.type=self.__class__.__name__

    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"Shape = {self.__class__.__name__}, area = {self.get_area()}, perimeter = {self.get_perimeter()}"

    def __repr__(self):
        return f"{self.__class__.__name__} : {', '.join(f"{key}={val}" for key,val in vars(self).items())}"

    def __eq__(self, other):
        return isinstance(other, Shape) and self.get_area() == other.get_area()

    def __lt__(self, other):
        return isinstance(other, Shape) and self.get_area() < other.get_area()

    def __le__(self, other):
        return isinstance(other, Shape) and self.get_area() <= other.get_area()

