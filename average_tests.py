#!/usr/bin/env python3
import unittest
from average import average

class AverageTests(unittest.TestCase):
    def test_math(self):
        self.assertEqual(average([1., 2., 3.]), 2.)
        self.assertEqual(average([99999., 2., 3.]), 33334.666666666664)

    def test_type(self):
        with self.assertRaises(TypeError):
            average(5)
        with self.assertRaises(TypeError):
            average("Hello, world!")

    def test_elem_type(self):
        with self.assertRaises(TypeError):
            average([1., 2., "Hello!"])
        with self.assertRaises(TypeError):
            average([7])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            average([])

if __name__ == '__main__':
    unittest.main()
