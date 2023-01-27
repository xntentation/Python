import math
class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
    # zwraca "x/y" lub "x" dla y=1
    def __str__(self):
        r = ""
        if(self.y != 1.0):
            r = f"{self.x}/{self.y}"
        else:
            r = f"{self.x}"
        return r
    
    # zwraca "Frac(x, y)"
    def __repr__(self):
        return f"Frac({self.x}, {self.y})"

    #def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    # Py2.7 i Py3
    def __eq__(self, other):
        if(isinstance(other,Frac)):
            if(self.x == other.x and self.y == other.y):
                return True
            else:
                return False
        elif (isinstance(other,int)):
            if(self.x == 0 and other == 0):
                return True
            elif(self.x < self.y):
                return False
            elif(self.x > self.y and self.x % self.y == 0):
                if(self.x//self.y == other):
                    return True
                else:
                    return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        f1 = float(self.x / self.y)
        f2 = float(other.x / other.y)
        return f1 < f2

    def __le__(self, other):
        f1 = float(self.x / self.y)
        f2 = float(other.x / other.y)
        return f1 <= f2        

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other): pass  # frac1 + frac2

    def __sub__(self, other): pass  # frac1 - frac2

    def __mul__(self, other): pass  # frac1 * frac2

    # frac1 / frac2, Py2
    def __div__(self, other):
        f = Frac(self.x * other.y , self.y * other.x)
        gcd = math.gcd(f.x, f.y)
        f.x = f.x / gcd
        f.y = f.y / gcd
        return f

    # frac1 / frac2, Py3
    def __truediv__(self, other):
        f = Frac(self.x * other.y , self.y * other.x)
        gcd = math.gcd(f.x, f.y)
        f.x = f.x / gcd
        f.y = f.y / gcd
        return f
    
    # frac1 // frac2, opcjonalnie
    def __floordiv__(self, other):
        l = self.x * other.y
        m = self.y * other.x
        return l//m

    # frac1 % frac2, opcjonalnie
    def __mod__(self, other):
        l = self.x * other.y
        m = self.y * other.x
        return l%m
        

    # operatory jednoargumentowe
    # +frac = (+1)*frac
    def __pos__(self): 
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    # float(frac)
    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def test_str(self):
        f1 = Frac(2,3)
        f2 = Frac(2,1)
        self.assertEqual(f1.__str__(), "2/3")
        self.assertEqual(f2.__str__(), "2")
    
    def test_rep(self):
        f = Frac(2,3)
        self.assertEqual(f.__repr__(), "Frac(2, 3)")
    
    def test_eq(self):    
        f1 = Frac(2,3)
        f2 = Frac(2,1)
        self.assertTrue(f1 == f1)
        self.assertFalse(f1 != f1)
        self.assertTrue(f1 != f2)
    
    def test_lt(self):
        f1 = Frac(2,3)
        f2 = Frac(2,1)
        self.assertTrue(f1 < f2)
        self.assertTrue(f2 > f1)
    
    def test_le(self):
        f1 = Frac(2,3)
        f2 = Frac(2,1)
        self.assertTrue(f1 <= f1)
        self.assertTrue(f2 >= f1)

        self.assertTrue(f1 <= f2)
        self.assertTrue(f2 >= f1)

    def test_div(self):
        f1 = Frac(2,3)
        f2 = Frac(2,3)
        f = f1 / f2
        self.assertEqual(f,Frac(1,1))
    
    def test_div(self):
        f1 = Frac(8,3)
        f2 = Frac(2,3)
        f = f1 // f2
        self.assertEqual(f,4)
    
    def test_mod(self):
        f1 = Frac(8,3)
        f2 = Frac(2,3)
        f3 = Frac(1,1)
        f = f1 % f2
        self.assertEqual(f,0)
        
        f = f2 % f3
        self.assertEqual(f,2)
    
    def test_float(self):
        f1 = Frac(8,3)
        f = float(f1)
        self.assertEqual(f,8/3)
        
    def test_hash(self):
        self.assertTrue(set([2]) == set([Frac(2)]))
        self.assertTrue(set([2]) == set([Frac(2)]))
        
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy