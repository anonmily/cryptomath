import unittest
from .baby_giant_step import babygiantstep

class TestModArithmetic(unittest.TestCase):
    def test_find_x_for_mod(self):
        p = 200003000003
        g = 3
        A = 387420489
        x = babygiantstep(p,g,A)
        A_check = pow(g, x, p)
        self.assertEqual(A_check, A)