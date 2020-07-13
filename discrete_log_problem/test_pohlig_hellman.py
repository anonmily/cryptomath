import unittest
from .pohlig_hellman import pohlig_hellman

class TestPohligHellman(unittest.TestCase):
    def test_pohlig_hellman_1(self):
        g = 23
        h = 9689
        p = 11251
        x = pohlig_hellman(g, h, p)
        self.assertEqual(x, 4261)
        self.assertEqual(pow(g, x, p), h)
    
    def test_pohlig_hellman_2(self):
        g = 15
        h = 131
        p = 337
        x = pohlig_hellman(g, h, p)
        self.assertEqual(x, 236)
        self.assertEqual(pow(g, x, p), h)