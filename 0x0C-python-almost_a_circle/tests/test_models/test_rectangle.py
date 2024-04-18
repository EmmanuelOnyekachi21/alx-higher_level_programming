"""
This module contains unit tests for the Rectangle class.

The Rectangle class represents a geometric rectangule shape.
It is defined in the models.rectangle module.
These unit tests ensure that the Rectangle class behaves as expected,
covering various scenarios and edge cases.
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A class for unit tests of the Rectangle class.

    This class inherits from unittest.TestCase and contains various
    test cases to ensure the correct behavior of the Rectangle class.

    Methods:
    """

    def test_all_attributes_provision(self):
        """Test case to ensure all attributes are initialized properly."""
        r1 = Rectangle(10, 9, 5, 6, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 9)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 3)

        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 12)

    def test_initialize_some(self):
        """Test case to ensure some attributes are initialized properly."""
        r1 = Rectangle(15, 30, 46)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 46)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_negative_values(self):
        """Test case to ensure the class handles negative values correctly."""
        r1 = Rectangle(-5, -10, -15, -20)
        self.assertEqual(r1.width, -5)
        self.assertEqual(r1.height, -10)
        self.assertEqual(r1.x, -15)
        self.assertEqual(r1.y, -20)
        self.assertEqual(r1.id, 2)

    def test_zero_values(self):
        """Test case to ensure the class handles zero values correctly."""
        r1 = Rectangle(0, 0, 0, 0)
        self.assertEqual(r1.width, 0)
        self.assertEqual(r1.height, 0)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 3)
