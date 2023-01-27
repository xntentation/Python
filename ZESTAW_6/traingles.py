from points import Point
import math
class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
    
    # "[(x1, y1), (x2, y2), (x3, y3)]"
    def __str__(self): 
        return f"[({self.pt1.x},{self.pt1.y}),({self.pt2.x},{self.pt2.y}),({self.pt3.x},{self.pt3.y})]"

    # "Triangle(x1, y1, x2, y2, x3, y3)"
    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
    # niezależnie od kolejności pt1, pt2, pt3.
    # obsługa tr1 == tr2
    def __eq__(self, other):
        v_set = {(self.pt1.x,self.pt1.y),(self.pt2.x,self.pt2.y),(self.pt3.x,self.pt3.y)}
        return ((other.pt1.x,other.pt1.y) in v_set) and ((other.pt2.x,other.pt2.y) in v_set) and ((other.pt3.x,other.pt3.y) in v_set)
        
    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other
    
    # zwraca środek (masy) trójkąta
    def center(self):
        return ((self.pt1.x + self.pt2.x + self.pt3.x) / 3.0,(self.pt1.y + self.pt2.y + self.pt3.y) / 3.0)

    # pole powierzchni
    def area(self):
        a = math.sqrt((self.pt1.x - self.pt2.x)**2 + (self.pt1.y - self.pt2.y)**2)
        b = math.sqrt((self.pt1.x - self.pt3.x)**2 + (self.pt3.y - self.pt3.y)**2)
        c = math.sqrt((self.pt2.x - self.pt3.x)**2 + (self.pt2.y - self.pt3.y)**2)
        p = (a + b + c) / 2.0
        S = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return S

    # przesunięcie o (x, y)
    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        
        self.pt2.x += x
        self.pt2.y += y
        
        self.pt3.x += x
        self.pt3.y += y

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):
    def test_str(self):
        tri = Triangle(0,0,5,5,0,5)
        self.assertEqual(tri.__str__(),"[(0,0),(5,5),(0,5)]")
    
    def test_repr(self):
         tri = Triangle(0,0,5,5,0,5)
         self.assertEqual(tri.__repr__(),"Triangle(0, 0, 5, 5, 0, 5)")
         
    def test_eq(self):
        tri1 = Triangle(0,0,5,5,0,5)
        tri2 = Triangle(5,5,0,0,0,5)
        tri3 = Triangle(0,5,5,5,0,0)
        self.assertEqual(tri1, tri2)
        self.assertEqual(tri2, tri3)
        self.assertEqual(tri3, tri1)
    
    def test_center(self):
        tri = Triangle(0,0,0,5,5,0)
        self.assertEqual(tri.center(), (5/3,5/3))
    
    def test_area(self):
        tri = Triangle(0,0,0,5,5,0)
        self.assertEqual(tri.area(), 0.5*5*5)
    
    def test_move(self):
        tri = Triangle(0,0,0,5,5,0)
        tri.move(0,5)
        self.assertEqual(tri.center(), (5/3,5+5/3))
        

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy