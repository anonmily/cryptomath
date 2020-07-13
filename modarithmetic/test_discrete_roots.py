import unittest
from .discrete_roots import get_discrete_root, get_composite_discrete_root

class TestGetDiscreteRoot(unittest.TestCase):
    def test_get_discrete_root(self):
        x1, x2 = get_discrete_root(2201, 4127)
        self.assertEqual(x1, 3718)
        self.assertEqual(x2, -3718)
    
    def test_get_composite_discrete_root(self):
        roots = get_composite_discrete_root(197, 437)
        self.assertListEqual(roots, [144, 201, 236, 293])