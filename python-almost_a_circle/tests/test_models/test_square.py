import unittest
from models.square import Square
import os.path
import io 
import sys

class TestBase(unittest.TestCase):
    def test_square_assignments(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)
        with self.assertRaises(TypeError):
            s4 = Square("1")
        with self.assertRaises(TypeError):
            s4 = Square(1, "2")
        with self.assertRaises(TypeError):
            s2 = Square(1, 2, "3")
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)
        with self.assertRaises(ValueError):
            s1 = Square(-1)
        with self.assertRaises(ValueError):
            s1 = Square(1, -2)
        with self.assertRaises(ValueError):
            s1 = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            s1 = Square(0)
    def test_square_area(self):
        s1 = Square(1)
        self.assertEqual(s1.area(), 1)
    def test_square_str(self):
        s1 = Square(1, 1, 1, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 1/1 - 1")

    def test_square_display(self):
        s1 = Square(1, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n #\n")
        s2 = Square(1, 1)
        output = io.StringIO()
        sys.stdout = output
        s2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), " #\n")
        s3 = Square(1)
        output = io.StringIO()
        sys.stdout = output
        s3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")
    def test_square_to_dictionary(self):
        s1 = Square(1, 1, 1, 1)
        self.assertEqual(s1.to_dictionary(), {'x': 1, 'y': 1, 'id': 1, 'size': 1})
    def test_square_update(self):
        s1 = Square(1)
        s1.update(89)
        self.assertEqual(s1.id, 89)
        s1.update(89, 1)
        self.assertEqual(s1.size, 1)
        s1.update(89, 1, 2)
        self.assertEqual(s1.x, 2)
        s1.update(89, 1, 2, 3)
        self.assertEqual(s1.y, 3)
        s2 = Square(1)
        s2.update(**{ 'id': 89 })
        self.assertEqual(s2.id, 89)
        s2.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s2.size, 1)
        s2.update(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s2.x, 2)
        s2.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s2.y, 3)
    def test_square_create(self):
        s1 = Square.create(**{ 'id': 89 })
        self.assertEqual(s1.id, 89)
        s1 = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s1.size, 1)
        s1 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s1.x, 2)
        s1 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s1.y, 3)
    def test_square_save_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file([Square(1, 2)])
    def test_square_load_from_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        loaded = Square.load_from_file()
        """
        self.assertEqual(str([]), "[]")
        Square.save_to_file(Square(1, 1, 1, 1, 1))
        loaded = Square.load_from_file()
        self.assertEqual(loaded, {'x': 1, 'y': 1, 'id': 1, 'height': 1, 'width': 1})
        """
