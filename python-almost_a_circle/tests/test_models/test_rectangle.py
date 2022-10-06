#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rect(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        with self.assertRaises(TypeError):
            r2 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, 3, "4")
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)