#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rect(self):
        self.assertEqual(3, Rectangle(1, 2).id)

    def test_rect1(self):
        self.assertEqual(4, Rectangle(1, 2, 3).id)

    def test_rect3(self):
        self.assertEqual(5, Rectangle(1, 2, 3, 4).id)