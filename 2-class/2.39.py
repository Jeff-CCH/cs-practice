"""
Develop an inheritance hierarchy based upon a Polygon class that has abstract methods area( ) and perimeter( ). Implement classes Triangle, Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base class, with the obvious meanings for the area( ) and perimeter( ) methods. Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectan- gle, and Square, that have the appropriate inheritance relationships. Fi- nally, write a simple program that allows users to create polygons of the various types and input their geometric dimensions, and the program then outputs their area and perimeter. For extra effort, allow users to input polygons by specifying their vertex coordinates and be able to test if two such polygons are similar.
"""

class Polygon(object):
    def area(self):
        pass
    def perimeter(self):
        pass

class Quadrilateral(Polygon): 
class Pentagonl(Polygon): 
class Hexagon(Polygon): 
class Octagon(Polygon): 
class IsoscelesTriangle(Polygon): 
class EquilateralTriangle(Polygon): 
class Rectangle(Polygon): 
class Square(Polygon): 
