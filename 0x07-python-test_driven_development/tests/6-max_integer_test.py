#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A test suite for the max_integer function.

    This class contains multiple test methods to verify the correctness
    of the max_integer function under various conditions. Each test method
    checks a specific aspect of the function's behavior, including its
    handling of regular lists, unordered lists, empty lists, lists containing
    negative numbers, and lists with duplicate maximum values.

    Methods:
        test_regular_case(self): Tests max_integer with a regular list
        test_empty_list(self): Test max_integer with an empty list
        test_unordered_list(self): Test max_integer with an unordered list.
        test_negative_numbers(self):  test max_integer with a list
                                    containig negative numbers.
    """

    def test_regular_case(self):
        """Tets max_integer with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test max_integer with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test max_integer with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicate_max(self):
        """Test max_integer with a list containing duplicate maximum values"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

if __name__ == "__main__":
    unittest.main()
