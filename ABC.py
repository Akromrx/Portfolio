import numpy as np
from abc import ABC, abstractclassmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractclassmethod
    def area(self):
        pass 
    
    @abstractclassmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r, color):
        super().__init__(color)
        self.r = r
    
    def area(self): # required method defined in Shape class (1)
        return np.pi * self.r ** 2
    
    def perimeter(self): # (1)
        return 2 * np.pi * r 



# C1 = Circle(5, 'White')
# print(C1.area())
