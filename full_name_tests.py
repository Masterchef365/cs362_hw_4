#!/usr/bin/env python3
import unittest
from full_name import full_name

class FullNameTests(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(full_name("Louis", "Armstrong"), "Louis Armstrong")
        self.assertEqual(full_name("John", "Wick"), "John Wick")
        self.assertEqual(full_name("Duncan", "Freeman"), "Duncan Freeman")

    def test_type(self):
        with self.assertRaises(TypeError):
            full_name("one", 1.)
        with self.assertRaises(TypeError):
            full_name(60., "nine")

    def test_non_empty(self):
        with self.assertRaises(ValueError):
            full_name("I'm just like", "")
        with self.assertRaises(ValueError):
            full_name("", "what")

if __name__ == '__main__':
    unittest.main()
