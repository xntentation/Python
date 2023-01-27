from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return f"[({self.pt1.x},{self.pt1.y}),({self.pt2.x},{self.pt2.y})]"

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    # obsługa rect1 == rect2
    def __eq__(self, other):
        if(self.pt1 == other.pt1 and self.pt2 == other.pt2):
            return True
        else:
            return False
            
    # obsługa rect1 != rect2
    def __ne__(self, other):        
        return not self == other

    # zwraca środek prostokąta
    def center(self):
        return ((self.pt1.x+self.pt2.x) / 2.0,(self.pt1.y + self.pt2.y) / 2.0)
    
    # pole powierzchni
    def area(self):
        w = abs(self.pt1.x - self.pt2.x)
        h = abs(self.pt1.y - self.pt2.y)
        return w * h
    
    # przesunięcie o (x, y)
    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        
        self.pt2.x += x
        self.pt2.y += y

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test_init(self):
        pass
        #p = Point(7,-9)
        #self.assertEqual(p.x == 7, p.y == -9)
    
    def test_str(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.__str__(),"[(0,0),(5,5)]")
    
    def test_repr(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.__repr__(),"Rectangle(0, 0, 5, 5)")
        
    def test_eq(self):
        rec1 = Rectangle(0,0,5,5)
        rec2 = Rectangle(0,0,-5,-5)
        self.assertTrue(rec1 == rec1)
        self.assertTrue(rec2 == rec2)
        self.assertTrue(rec1 != rec2)
        self.assertTrue(rec2 != rec1)
    
    def test_center(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.center(), (2.5,2.5))
    
    def test_area(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.area(), 25.0)
        
    def test_move(self):
        rec = Rectangle(0,0,5,5)
        rec.move( -2.5, -2.5)
        self.assertEqual(rec.center(), (0.0,0.0))
        
        
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy