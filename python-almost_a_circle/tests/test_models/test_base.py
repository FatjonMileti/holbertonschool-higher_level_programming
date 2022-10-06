import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)
    def test_3(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)
