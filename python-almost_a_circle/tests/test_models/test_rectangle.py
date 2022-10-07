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
            r5 = Rectangle(1, 2, 3, "4")
        r6 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r6.id, 5)
        with self.assertRaises(ValueError):
            r7 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r9 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r10 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r11 = Rectangle(1, 2, -3)