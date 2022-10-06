import imp
import unittest
import os
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
    
    def test_1(self):
        b0 = Base()
        self.assertEqual(b0.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)