#!/usr/bin/python3
import unittest
import os.path
import io 
import sys
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
        with self.assertRaises(ValueError):
            r12 = Rectangle(1, 2, 3, -4)
    def test_rectangle_area(self):
        r13 = Rectangle(1, 1)
        self.assertEqual(r13.area(), 1)
    def test_rectangle_str(self):
        r14 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r14.__str__(), "[Rectangle] (1) 1/1 - 1/1")
    def test_rectangle_display(self):
        r15 = Rectangle(1, 1, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        r15.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n #\n")
        r16 = Rectangle(1, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        r16.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), " #\n")
        r17 = Rectangle(1, 1)
        output = io.StringIO()
        sys.stdout = output
        r17.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")
    def test_to_dictionary(self):
        r18 = Rectangle(1, 2, 3, 4, 5)
        rect_dict = {'id': 5, 'x': 3, 'y': 4, 'width': 1, 'height': 2}
        self.assertEqual(rect_dict, r18.to_dictionary())
    def test_update_zero_arg(self):
        r19 = Rectangle(1, 2, 3, 4, 5)
        r19.update()
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r19))
    def test_rectangle_create(self):
        r20 = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(r20.id, 89)
        r21 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(r21.width, 1)
        r22 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r22.height, 2)
        r23 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r23.x, 3)
        r24 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r24.y, 4)
    def test_rectangle_load_from_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        loaded = Rectangle.load_from_file()

        r25 = Rectangle(5, 5)
        r26 = Rectangle(8, 2, 5, 5)

        l_input = [r25, r26]
        Rectangle.save_to_file(l_input)
        l_output = Rectangle.load_from_file()

        for i in range(len(l_input)):
            self.assertEqual(l_input[i].__str__(), l_output[i].__str__())