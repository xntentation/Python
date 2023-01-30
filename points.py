import math
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y
    
    # zwraca string "(x, y)"
    def __str__(self):
        return f"({self.x},{self.y})"
        
    # zwraca string "Point(x, y)"
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    
    # obsługa point1 == point2
    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False
    
    # obsługa point1 != point2
    def __ne__(self, other):        
        return not self == other

    # Punkty jako wektory 2D.
    # v1 + v2
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # v1 - v2
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    # v1 * v2, iloczyn skalarny, zwraca liczbę
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
    def cross(self, other):         
        return self.x * other.y - self.y * other.x
    
    # długość wektora
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.
'''
p1 = Point(5,-5)
p2 = Point(5,-6)
print(p1)
print(p1.__repr__())
print(p1 == p2)

print(p1+p2)
print(p1*p2)

print(hash(p1))
print(hash(p2))
'''

import unittest

class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point(7,-9)
        self.assertEqual(p.x == 7, p.y == -9)
    
    def test_str(self):
        p = Point(-1,5)
        self.assertEqual(p.__str__(),"(-1,5)")
    
    def test_rep(self):
        p = Point(-1,5)
        self.assertEqual(p.__repr__(),"Point(-1,5)")
    
    def test_eq(self):
        p1 = Point(0,8)
        p2 = Point(9,20)
        self.assertTrue(p1 == p1)
        self.assertTrue(p2 == p2)
        self.assertFalse(p1 == p2)
        self.assertFalse(p2 == p1)
    
    def test_neq(self):
        p1 = Point(0,8)
        p2 = Point(9,20)
        self.assertFalse(p1 != p1)
        self.assertFalse(p2 != p2)
        self.assertTrue(p1 != p2)
        self.assertTrue(p2 != p1)
    
    def test_add(self):
        p1 = Point(-9,-15)
        p2 = Point(5,22)
        p = p1 + p2
        self.assertEqual(p.x, -9 + 5)
        self.assertEqual(p.y, -15 + 22)
        
    def test_sub(self):
        p1 = Point(-9,-15)
        p2 = Point(5,22)
        p = p1 - p2
        self.assertEqual(p.x, -9 - 5)
        self.assertEqual(p.y, -15 - 22)
    
    def test_mul(self):
        p1 = Point(-9,-15)
        p2 = Point(5,22)
        self.assertEqual(p1 * p2, p1.x * p2.x + p1.y * p2.y)
        self.assertEqual(p2 * p1, p1.x * p2.x + p1.y * p2.y)
        
    def test_mul(self):
        p1 = Point(-9,-15)
        p2 = Point(5,22)
        self.assertEqual(p1.cross(p2),  p1.x * p2.y - p1.y * p2.x)
        self.assertEqual(p2.cross(p1), -(p1.x * p2.y - p1.y * p2.x))
    
    def test_len(self):
        p = Point(-9,-15)
        self.assertEqual(p.length(), math.sqrt(p.x**2 + p.y**2))
    
    def test_hash(self):
        p1 = Point(-9,-15)
        p2 = Point(5,22)
        self.assertNotEqual(hash(p1), hash(p2))
        
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy