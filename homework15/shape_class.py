from abc import ABC, abstractmethod
from cmath import sqrt
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, h, v):
        self.h = h
        self.v = v
        
    def area(self):
        return self.h * self.v
    
    def perimeter(self):
        return 2 * (self.h + self.v) 
   
    
class Triangle(Shape):
    def __init__(self, h, v):
        self.h = h
        self.v = v
        
    def area(self):
        return self.h * self.v * 1/2
    
    def perimeter(self):
        return self.h + self.v + sqrt(pow(self.h, 2) + pow(self.v, 2))


class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return math.pi * self.r * self.r
    
    def perimeter(self):
        return math.pi * self.r * 2

    
class RegularHexagon(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return (3 * sqrt(3) * pow(self.r, 2))/2
    
    def perimeter(self):
        return self.r * 6

    def __repr__(self):
        return (("사각형(밑변={}, 높이={}").format(self.h self.v))

    def __repr__(self):
        return

def main():
    
    shapes = [Rectangle(4, 5),
              Triangle(4, 5),
              Circle(4), 
              RegularHexagon(4)]
    
    for shape in shapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())


if __name__ == "__main__":
    main()

    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a+b)






