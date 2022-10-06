#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rect(self):
        self.assertEqual(2, Rectangle(1, 2).id)

    def test_rect1(self):
        self.assertEqual(1, Rectangle(1, 2, 3).id)

    def test_rect3(self):
        self.assertEqual(2, Rectangle(1, 2, 3, 4).id)