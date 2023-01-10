import math 
# frac1 + frac2
def add_frac(frac1, frac2): 
    l1 = frac1[0]
    l2 = frac2[0]
    m1 = frac1[1]
    m2 = frac2[1]
    l = l1*m2 + l2*m1
    m = m1*m2
    gcd = math.gcd(l,m)
    f = [ l /gcd , m / gcd ]
    return f

# frac1 - frac2
def sub_frac(frac1, frac2):
    l1 = frac1[0]
    l2 = frac2[0]
    m1 = frac1[1]
    m2 = frac2[1]
    l = l1*m2 - l2*m1
    m = m1*m2
    gcd = math.gcd(l,m)
    f = [ l /gcd , m / gcd ]
    return f

# frac1 * frac2
def mul_frac(frac1, frac2):
    l1 = frac1[0]
    l2 = frac2[0]
    m1 = frac1[1]
    m2 = frac2[1]
    l = l1 * l2
    m = m1 * m2
    gcd = math.gcd(l,m)
    f = [ l /gcd , m / gcd ]
    return f

# frac1 / frac2
def div_frac(frac1, frac2):
    l1 = frac1[0]
    l2 = frac2[0]
    m1 = frac1[1]
    m2 = frac2[1]
    l = l1 * m2
    m = m1 * l2
    gcd = math.gcd(l,m)
    f = [ l /gcd , m / gcd ]
    return f
# bool, czy dodatni
def is_positive(frac):
    l = frac[0]
    m = frac[1]
    pos = False
    if( l > 0 and m > 0 ):
        pos = True
    elif(l < 0 and m < 0):
        pos = True
    return pos
        
    
# bool, typu [0, x]
def is_zero(frac):
    return frac[0] == 0

# -1 | 0 | +1
def cmp_frac(frac1, frac2):
  if(frac2float(frac1) > frac2float(frac2)):
    return -1
  elif(frac2float(frac1) < frac2float(frac2)):
    return 1
  else:
    return 0          
# konwersja do float
def frac2float(frac):
    return frac[0] / frac[1] 

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([3, 2], [1, 3]), [1, 2])

    def test_div_frac(self): 
        self.assertEqual(div_frac([3, 1], [3, 1]), [1, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([-3, 1]), False)
        self.assertEqual(is_positive([1, 8]), True)
        self.assertEqual(is_positive([1, -8]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 1]), True)
        
    def test_cmp_frac(self): 
        self.assertEqual(cmp_frac([2,3], [2,3]), 0)
        self.assertEqual(cmp_frac([4,3], [2,3]), -1)
        self.assertEqual(cmp_frac([2,3], [5,3]), +1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
