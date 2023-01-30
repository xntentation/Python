from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    
    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"
    
    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    # obsługa rect1 == rect2
    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    # zwraca środek prostokąta
    def center(self):
        return ((self.pt1.x+self.pt2.x) / 2, (self.pt1.y+self.pt2.y) / 2)
    
    # pole powierzchni
    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)
    
    # przesunięcie o (x, y)
    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

    # część wspólna prostokątów    
    def intersection(self, other):
        if(not self.intersect(self, other)):
            return Rectangle(0,0,0,0)
        else:
            r1 = self
            r2 = other
            return Rectangle(max(r1.pt1.x, r2.pt1.x), max(r1.pt1.y, r2.pt1.y), min(r1.pt2.x, r2.pt2.x), min(r1.pt2.y, r2.pt2.y))
    
    def intersect(self, r1, r2):
        return (r1.pt1.x <= r2.pt2.x) and (r1.pt2.x) >= r2.pt1.x and (r1.pt1.y <= r2.pt2.y) and (r1.pt2.y >= r2.pt1.y)
    
    # prostąkąt nakrywający oba
    def cover(self, other):
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    # zwraca krotkę czterech mniejszych
    # A-------B   po podziale  A---B---C
    # |       |                |   |   |
    # |       |                D---E---F
    # |       |                |   |   |
    # D-------C                G---H---I
    def make4(self):
        A = (self.pt1.x, self.pt2.y)
        B = ((self.pt1.x+self.pt2.x) / 2, self.pt2.y)
        C = (self.pt2.x, self.pt2.y)
        D = (self.pt1.x, (self.pt1.y+self.pt2.y)/2)
        E = ((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)
        F = (self.pt2.x, (self.pt1.y+self.pt2.y)/2)
        G = (self.pt1.x, self.pt1.y)
        H = ((self.pt1.x+self.pt2.x)/2, self.pt1.y)
        I = (self.pt2.x, self.pt1.y)
        # ABDE
        rec1 = Rectangle(D[0], D[1], B[0], B[1])
        # BCEF
        rec2 = Rectangle(E[0], E[1], C[0], C[1])
        # DEGH
        rec3 = Rectangle(G[0], G[1], E[0], E[1])
        # EFHI
        rec4 = Rectangle(H[0], H[1], F[0], F[1])
        return (rec1,rec2,rec3,rec4)


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test_str(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.__str__(), "[(0, 0), (5, 5)]")

    def test_repr(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.__repr__(), "Rectangle(0, 0, 5, 5)")
    
    def test_eq(self):
        rec1 = Rectangle(0,0,5,5)
        rec2 = Rectangle(0,0,2,2)
        self.assertTrue(rec1 == rec1)
        self.assertTrue(rec1 != rec2)
    
    def test_center(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.center(), (2.5,2.5))
        
    def test_area(self):
        rec = Rectangle(0,0,5,5)
        self.assertEqual(rec.area(), 25)
    
    def test_move(self):
        rec = Rectangle(0,0,5,5)
        rec.move(-5, -5)
        self.assertEqual(rec.__str__(), "[(-5, -5), (0, 0)]")
    
    def test_intersection(self):
        rec1 = Rectangle(0,0,5,5)
        rec2 = Rectangle(0,0,10,10)
        rec3 = Rectangle(2,2,5,5)
        p1 = rec1.intersection(rec2)
        p2 = rec1.intersection(rec1)
        p3 = rec1.intersection(rec3)
        self.assertEqual(p1.__str__(), "[(0, 0), (5, 5)]")
        self.assertEqual(p2.__str__(), "[(0, 0), (5, 5)]")
        self.assertEqual(p3.__str__(), "[(2, 2), (5, 5)]")
        
    def test_cover(self):
        rec1 = Rectangle(0,0,5,5)
        rec2 = Rectangle(-1,-2,2,2)
        cov = rec1.cover(rec2)
        self.assertEqual(cov.__str__(), "[(-1, -2), (5, 5)]")
    
    def test_make4(self):
        rec = Rectangle(-2,-2,2,2)
        k = rec.make4()
        self.assertEqual(k[0].__str__(), "[(-2, 0.0), (0.0, 2)]")
        self.assertEqual(k[1].__str__(), "[(0.0, 0.0), (2, 2)]")
        self.assertEqual(k[2].__str__(), "[(-2, -2), (0.0, 0.0)]")
        self.assertEqual(k[3].__str__(), "[(0.0, -2), (2, 0.0)]")
        
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    