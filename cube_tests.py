#!/usr/bin/env python3
import unittest
from cube import cube

class CubeTests(unittest.TestCase):
    def test_math(self):
        self.assertEqual(cube(1., 2., 3.), 6.)
        self.assertEqual(cube(9., 8., 7.), 504.)
        self.assertEqual(cube(0., 8., 7.), 0.)
        self.assertEqual(cube(9., 0., 7.), 0.)
        self.assertEqual(cube(9., 8., 0.), 0.)

    def test_type(self):
        with self.assertRaises(TypeError):
            cube("one", 1., 2.)
        with self.assertRaises(TypeError):
            cube(9, 1., 2.)

    def test_negative(self):
        with self.assertRaises(ValueError):
            cube(-9., 1., 8.)
        with self.assertRaises(ValueError):
            cube(9., -1., 8.)
        with self.assertRaises(ValueError):
            cube(9., 1., -8.)

if __name__ == '__main__':
    unittest.main()
