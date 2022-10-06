#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rect(self):
        self.assertEqual(2, Rectangle(1, 2).id)

    def test_get_width(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(1, rect.width)