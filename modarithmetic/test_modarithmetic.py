import unittest
from .modarithmetic import find_x_for_mod, get_mod_inverse, xgcd

class TestModArithmetic(unittest.TestCase):
    def test_find_x_for_mod(self):
        f = lambda x: 5*x
        c = 4
        m = 3
        x = find_x_for_mod(f, c, m, print_all=True)
        self.assertEqual(x, 2)
        self.assertEqual(f(x) % m, c % m)
    
    def test_get_mod_inverse(self):
        a = 2
        m = 7
        a_inv = get_mod_inverse(a, m)
        self.assertEqual( a*a_inv % m, 1)
    
    def test_xgcd(self):
        a = 4864
        b = 3458
        d, x, y = xgcd(a, b)
        self.assertEqual(a*x + b*y, d)