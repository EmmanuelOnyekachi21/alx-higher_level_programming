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
import os


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
        self.assertEqual(r.id, 5)

        a = Rectangle(2, 4)
        self.assertEqual(a.width, 2)
        self.assertEqual(a.height, 4)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 6)

        c = Rectangle(1, 2, id=200)
        self.assertEqual(c.id, 200)

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

    def test_str(self):
        """Test the __str__ method"""
        captured_output = StringIO()
        sys.stdout = captured_output

        a = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        print(a)
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output.truncate(0)
        captured_output.seek(0)

        b = Rectangle(2, 1, id=10)
        expected = "[Rectangle] (10) 0/0 - 2/1\n"
        print(b)
        self.assertEqual(captured_output.getvalue(), expected)

        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_display(self):
        """Testing the `display` method of the Rectangle class."""
        r = Rectangle(3, 2, 1, 1)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ###\n ###\n")

    def test_display_no_offset(self):
        """Test the display() method of the Rectangle class with no offset."""
        r = Rectangle(3, 2, 0, 0)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "###\n###\n")


class TestRectangleUpdate(unittest.TestCase):
    """A class to check the correctness of the `update()` method."""
    def test_update_with_id(self):
        """Testing with id"""
        z = Rectangle(2, 3, 4, 5, 8)
        captured = StringIO()
        sys.stdout = captured
        print(z)
        self.assertEqual(captured.getvalue(), "[Rectangle] (8) 4/5 - 2/3\n")

        captured.truncate(0)
        captured.seek(0)

        sys.stdout = sys.__stdout__

        z.update(89)
        captured = StringIO()
        sys.stdout = captured
        print(z)
        self.assertEqual(captured.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

        captured.truncate(0)
        captured.seek(0)

        sys.stdout = sys.__stdout__

        z.update(89, 1, 5)
        captured = StringIO()
        sys.stdout = captured
        print(z)
        self.assertEqual(captured.getvalue(), "[Rectangle] (89) 4/5 - 1/5\n")

        captured.truncate(0)
        captured.seek(0)

        sys.stdout = sys.__stdout__

        z.update(89, 5, 10, 12)
        captured = StringIO()
        sys.stdout = captured
        print(z)
        self.assertEqual(captured.getvalue(), "[Rectangle] (89) 12/5 - 5/10\n")

        captured.truncate(0)
        captured.seek(0)

        sys.stdout = sys.__stdout__

        with self.assertRaises(TypeError):
            z.update(89, "t")

        with self.assertRaises(TypeError):
            z.update(89, 5, 10.4)

    def test_update_name_errors(self):
        """Testing name errors with the update() method."""
        y = Rectangle(2, 3, 5)
        with self.assertRaises(NameError):
            y.update(t)

    def test_update_with_negative_values(self):
        """Test the update() method with negative values."""
        y = Rectangle(1, 2)
        y.update(15)
        self.assertEqual(y.id, 15)
        with self.assertRaises(ValueError):
            y.update(15, 1, 2, -3)


class TestRectangleUpdate(unittest.TestCase):
    """A class for unit tests of the Rectangle class update() method."""

    def setUp(self):
        """Set up a Rectangle instance before each test."""
        self.r1 = Rectangle(10, 20, 30, 40, 50)

    def test_update_with_args(self):
        """Test updating attributes with positional arguments."""
        self.r1.update(1, 2, 3, 4, 5)

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

    def test_update_with_kwargs(self):
        """Test updating attributes with keyword arguments."""
        self.r1.update(width=15, height=25, x=35, y=45)
        self.assertEqual(self.r1.width, 15)
        self.assertEqual(self.r1.height, 25)
        self.assertEqual(self.r1.x, 35)
        self.assertEqual(self.r1.y, 45)

    def test_update_with_both_args_and_kwargs(self):
        """
        Test updating attributes with both positional and keyword arguments.
        """
        self.r1.update(1, 2, 3, 4, 5, width=15, height=25, x=35, y=45)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 2)  # Args take precedence
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)


class TestRectangle_to_dictionary(unittest.TestCase):
    """
    Test cases for the Rectangle class focusing on the to_dictionary method.
    """
    def test_to_dictionary_empty(self):
        """
        Tests the to_dictionary method with an empty rectangle (no arguments).
        """
        r = Rectangle(1, 2)
        expected_dict = {
            "id": 10,
            "width": 1,
            "height": 2,
            "x": 0,
            "y": 0
            }
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_with_args(self):
        """
        Tests the to_dictionary method with arguments
        passed to the constructor.
        """
        r = Rectangle(10, 2, 1, 9, 5)
        expected_dict = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_after_update(self):
        """
        Tests the to_dictionary method after updating the rectangle attributes.
        """
        r = Rectangle(5, 3)
        r.update(width=8, height=4, x=2, y=1)
        expected_dict = {"id": 9, "width": 8, "height": 4, "x": 2, "y": 1}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_json_string_method(self):
        """Test the to_json_string() method."""

    def test_to_json_string(self):
        """Test case for to_json_string method."""
        r = Rectangle(5, 10)
        result = r.to_json_string([r.to_dictionary()])
        self.assertEqual(
            result,
            '[{"id": 11, "width": 5, "height": 10, "x": 0, "y": 0}]')

    def test_save_to_file(self):
        """Test the save_to_file() method."""
        r1 = Rectangle(10, 7, 2, 8, 6)
        r2 = Rectangle(id=1, height=2, width=3)

        # Call save_to_file method
        Rectangle.save_to_file([r1, r2])

        # Check if file was created.
        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))

        # Check if file content is correct
        with open(filename, "r") as file:
            content = file.read()
            exp = ('[{"id": 6, "width": 10, "height": 7, "x": 2, "y": 8}, '
                   '{"id": 1, "width": 3, "height": 2, "x": 0, "y": 0}]')
            self.assertEqual(content.strip(), exp)

        # Clean up
        os.remove(filename)

    def test_save_empty_list(self):
        filename = "Rectangle.json"
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove(filename)


class TestFromJSONString(unittest.TestCase):
    """Test cases for the from_json_string() method."""

    def test_rectangle_from_json_string(self):
        """Test the from_json_string() method for the Rectangle class."""

        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, list_input)

    def test_rectangle_empty_list(self):
        """Test with an empty string."""
        self.assertEqual(Rectangle.from_json_string([]), [])

    def test_zero_attributes(self):
        """Test with '0' attributes."""
        json_string = (
            '[{"id": 1, "width": 0, "height": 0, "x": 0, "y": 0}]')
        expected_output = (
                [{'id': 1, 'width': 0, 'height': 0, 'x': 0, 'y': 0}])
        self.assertEqual(
                Rectangle.from_json_string(json_string),
                expected_output)

    def test_negative_values(self):
        """Testing negative values..."""
        json_string = (
                '[{"id": 1, "width": -10, "height": -5, "x": 0, "y": 0}]')
        expected_output = (
                [{'id': 1, 'width': -10, 'height': -5, 'x': 0, 'y': 0}])
        self.assertEqual(
                Rectangle.from_json_string(json_string),
                expected_output)

    def test_large_values(self):
        """Test Large Values."""
        json_string = (
                '[{"id": 1, "width": 10000, "height": 5000, "x": 0, "y": 0}]')
        expected_output = (
                [{'id': 1, 'width': 10000, 'height': 5000, 'x': 0, 'y': 0}])
        self.assertEqual(
                Rectangle.from_json_string(json_string), expected_output)

    def test_rectangle_non_integer_values(self):
        """Testing with non-integer values..."""
        json_string = (
                '[{"id": 1, "width": 10.5, "height": 5.5, "x": 0, "y": 0}]')
        expected_output = (
                [{'id': 1, 'width': 10.5, 'height': 5.5, 'x': 0, 'y': 0}])
        self.assertEqual(
                Rectangle.from_json_string(json_string), expected_output)

    def test_rectangle_missing_keys(self):
        """Test with missing keys."""
        json_string = '[{"id": 1, "width": 10, "x": 0, "y": 0}]'
        expected_output = (
                [{'id': 1, 'width': 10, 'x': 0, 'y': 0}])
        self.assertEqual(
                Rectangle.from_json_string(json_string), expected_output)

    def test_create(self):
        """Test creatikng a Rectangle instance using the create class method.
        """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 4, 'x': 2, 'y': 1}
        r1 = Rectangle.create(**rectangle_dict)

        # Check if the created instance has the correct attributes.
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)


if __name__ == "__main__":
    unittest.main()
