#!/usr/bin/python3
""" This module houses test cases for rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Testing for the attributes
    """

    def test_attributes(self):
        r = Rectangle(10, 2, 5, 3, 7)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 7)

    def test_setters(self):
        r = Rectangle(10, 2, 5, 3, 7)

        r.width = 20
        r.height = 5
        r.x = 10
        r.y = 8

        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 8)

    def test_instantiation_normal(self):
        a = Rectangle(10, 2)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)

    def test_instantiation_normal2(self):
        a = Rectangle(10, 2, 2, 2,)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 2)

    def test_instantiation_normal3(self):
        a = Rectangle(10, 2, 2, 0, 12)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 12)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -5, 3)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 5, -3)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10.25, "hu", 4, 6, 20)
    def test_invalid_x_value(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.x = -5
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2)
            r.y = {}
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.y = -3
        self.assertEqual(str(context.exception), "y must be >= 0")

if __name__ == "__main__":
    unittest.main()
