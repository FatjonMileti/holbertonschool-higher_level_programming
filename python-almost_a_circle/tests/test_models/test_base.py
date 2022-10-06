import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base_assignments(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
    def test_base_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "null")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
    def test_base_from_json_string(self): 
        self.assertEqual(Base.from_json_string(None), [])
        with self.assertRaises(TypeError):
            Base.from_json_string([])
        self.assertEqual(Base.from_json_string('[{"id": 89 }]'), [ { 'id': 89 }])
