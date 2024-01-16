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

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_area2(self):
        a = Rectangle(5, 4, 1, 1)
        a.width = 6
        self.assertEqual(a.area(), 24)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (8) 1/0 - 5/5")

    def test_update_with_valid_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (9) 10/10 - 10/10")
        # Test the update method with different sets of arguments
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2)
        self.assertEqual(str(r), "[Rectangle] (2) 1/1 - 1/1")
        r.update(3, 2)
        self.assertEqual(str(r), "[Rectangle] (3) 1/1 - 2/1")
        r.update(4, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (4) 1/1 - 2/3")
        r.update(5, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (5) 4/1 - 2/3")
        r.update(6, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")

    def test_update_method_with_keyword_arguments(self):
        r = Rectangle(1, 1, 1, 1, 1)
        # Check the initial state
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")
        # Test the update method with keyword arguments
        r.update(height=2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/2")
        r.update(width=2, x=3)
        self.assertEqual(str(r), "[Rectangle] (1) 3/1 - 2/2")
        r.update(y=4, width=5, x=6, id=7)
        self.assertEqual(str(r), "[Rectangle] (7) 6/4 - 5/2")
        r.update(x=8, height=9, y=10, width=11)
        self.assertEqual(str(r), "[Rectangle] (7) 8/10 - 11/9")


if __name__ == "__main__":
    unittest.main()
