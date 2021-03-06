import unittest
import numpy as np
from .modarithmetic import find_x_for_mod, get_mod_inverse, xgcd
from .matrices import get_matrix_inverse
from .chinese_remainder import chinese_remainder_theorem

class TestFindXForMod(unittest.TestCase):
    def test_find_x_for_mod(self):
        f = lambda x: 5*x
        c = 4
        m = 3
        x = find_x_for_mod(f, c, m, verbose=True)
        self.assertEqual(x, 2)
        self.assertEqual(f(x) % m, c % m)

    def test_find_x_for_mod_nonverbose(self):
        f = lambda x: 5*x
        c = 4
        m = 3
        x = find_x_for_mod(f, c, m, verbose=False)
        self.assertEqual(x, 2)
        self.assertEqual(f(x) % m, c % m)

    def test_find_x_for_mod_with_string_f(self):
        f = '5*x'
        c = 4
        m = 3
        x = find_x_for_mod(f, c, m, verbose=True)
        self.assertEqual(x, 2)
        self.assertEqual(eval(f) % m, c % m)

class TestGetModInverse(unittest.TestCase):
    def test_get_mod_inverse(self):
        a = 2
        m = 7
        a_inv = get_mod_inverse(a, m)
        self.assertEqual( a*a_inv % m, 1)

class TestExtEuclidAlgorithm(unittest.TestCase):
    def test_xgcd(self):
        a = 4864
        b = 3458
        d, x, y = xgcd(a, b)
        self.assertEqual(a*x + b*y, d)

class TestMatrices(unittest.TestCase):
    def test_get_matrix_inverse_mod(self):
        a = [[1,3],[25,0]]
        a_inv = get_matrix_inverse(a, m=26)
        np.testing.assert_allclose(a_inv, [[0, 25],[9,9]])

class TestChineseRemainderTheorem(unittest.TestCase):
    def test_chin_remainder_thm_2_eqs(self):
        c, m = chinese_remainder_theorem([(3,7),(9,13)])
        self.assertEqual(c, 87)
        self.assertEqual(m, 91)

    def test_chin_remainder_thm_3_eqs(self):
        c, m = chinese_remainder_theorem([(6,9), (8,10), (5,11)])
        self.assertEqual(c, 258)
        self.assertEqual(m, 990)
    
    def test_chin_remainder_thm_4_eqs(self):
        c, m = chinese_remainder_theorem([
            (1,3), (1,4), (1,5), (0,7)
        ])
        self.assertEqual(c, 301)
        self.assertEqual(m, 3*4*5*7)