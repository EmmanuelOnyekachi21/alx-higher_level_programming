"""
This module contains unit tests for the Rectangle class.

The Rectangle class represents a geometric rectangule shape.
It is defined in the models.rectangle module.
These unit tests ensure that the Rectangle class behaves as expected,
covering various scenarios and edge cases.
"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


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
        r = Rectangle(15, 30, 46)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 46)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 4)

        a = Rectangle(2, 4)
        self.assertEqual(a.width, 2)
        self.assertEqual(a.height, 4)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 3)

        with self.assertRaises(TypeError):
            b = Rectangle(2)

    def test_exceeding_arguments(self):
        """
        Test case for when arguments provided to Rectangle exceeds
        the required arguments
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 5, 6, 7, 8)

    def test_zero_values(self):
        """Test case to ensure the class handles zero values correctly."""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0, 0, 0, 2)

    def test_non_integer_width(self):
        """Test case to ensure the class handles Exceptions correctly."""
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

    def test_non_integer_height(self):
        """test case to ensure the class handles exceptions correctly."""
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

    def test_non_integer_x(self):
        """Test case to ensure that the class handles Exceptions correctly."""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, {})

    def test_non_integer_y(self):
        """Test case to ensure that the class handles Exceptions correctly."""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 5, [])

    def test_width_less_than_zero(self):
        """Test case to ensure that the class handles Exceptions correctly."""
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)

    def test_height_less_than_zero(self):
        """Test case to ensure that the class handles Exceptions correctly."""
        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)

    def test_x_less_than_zero(self):
        """Test case to ensure that the class handles Exceptions correctly."""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -5)

    def test_y_less_than_zero(self):
        """Test case to ensure that the class handles Exceptions correctly."""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 5, -3)

    def test_invalid_id_type(self):
        """
        Test if providing a non-integer value for ID doesn't raise an
        exception.
        """
        r = Rectangle(10, 2, 5, 6, "3")
        self.assertEqual(r.id, "3")

        r = Rectangle(10, 2, 3, 5, 3.9)
        self.assertEqual(r.id, 3.9)

    def test_min_integer_values(self):
        """Test with minimum possible integer values."""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_max_integer_values(self):
        """Test with maximum possible integer values."""
        r = Rectangle(2147483647, 2147483647, 2147483647, 2147483647)
        self.assertEqual(r.width, 2147483647)
        self.assertEqual(r.height, 2147483647)
        self.assertEqual(r.x, 2147483647)
        self.assertEqual(r.y, 2147483647)

    def test_possible_name_errors(self):
        """
        Test case for possible name errors.
        """
        with self.assertRaises(NameError):
            a = Rectangle(2, t)

        with self.assertRaises(NameError):
            b = Rectangle(r, 4)

    def test_area(self):
        """Test the Area method in models.rectangle."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_non_integer_dimensions(self):
        """
        Test case to ensure area method handles rectangles with non-integer
        dimensions.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, "2")
        with self.assertRaises(TypeError):
            r = Rectangle("3", 2)

        with self.assertRaises(TypeError):
            r = Rectangle("3", "2")
    def test_non_integer_coordinates(self):
        """Test case to ensure area method handles non-integer coordinates."""
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, "x", 0)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, 0, "y")

    def test_display(self):
        """
        Test the output of the `Display` method of the `Rectangle` class.
        """
        # Redirect stdout to capture print output.
        captured_output = StringIO()
        sys.stdout = captured_output

        a = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        a.display()
        self.assertEqual(captured_output.getvalue(), expected_output)
        
        captured_output.truncate(0)
        captured_output.seek(0)

        r2 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        r2.display()
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Reset stdout
        sys.stdout = sys.__stdout__
