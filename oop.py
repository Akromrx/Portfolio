import numpy as np

class Shape:
    def __init__(self, shape):
        self.shape = shape

    def perimeter(self, *args):
        if self.shape.lower() == 'circle':
            if len(args) > 1:
                return -1   
            return (2 * np.pi * args[0]) 
        if self.shape.lower() == 'rectangle':
            return sum(args) * 2
    
    def area(self, *kwargs):
        kwargs = np.asarray(kwargs)
        if self.shape.lower() == 'triangle':
            s = (np.sum(kwargs)/2)
            p = np.sqrt(s - kwargs)
            return p

        elif self.shape.lower() == 'circle':
            a = np.pi * (kwargs**2)
            return a[0]
        
        elif self.shape.lower() == 'rectangle':
            return kwargs[0] * kwargs[1]
            
class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius
    
    def ChildPer(self):
        P = self.perimeter(self.radius)
        return P
    
    def ChildArea(self):
        A = self.area(self.radius)
        return A

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__('rectangle')
        self.a = a
        self.b = b
    
    def ChildPer(self):
        return self.perimeter(self.a, self.b)
    


C1: Circle = Circle(10)
print(C1.ChildPer())
print(C1.ChildArea())

R1: Rectangle = Rectangle(34, 9)
print(R1.ChildPer())

