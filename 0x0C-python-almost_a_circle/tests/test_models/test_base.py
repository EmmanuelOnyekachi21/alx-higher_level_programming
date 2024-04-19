from models.base import Base
import unittest
"""
This module defines various tests for the Base class.
"""


class TestBaseClass(unittest.TestCase):
    """
    A base class for unit tests.

    This class inherits from unittest.TestCase and serves as a base class
    for writing unit tests in the test suite. It provides common
    functionalities and setups reequired for testing various
    components of the system.

    Methods(s):
        test_empty:             Test when no value is provided.
        test_positive_id:       when id is +ve
        test_negative_id:       When id = -ve
        test_large_id:          Test with a large positive id value.
        test_zero_id:           Test with id value of zero.
        test_none_id:           Test with id value as None.
    """
    def test_empty(self):
        """Test when no value is provided."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_positive_id(self):
        """Tests that the value of id is properly assigned a positive value."""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base(1)
        self.assertEqual(b5.id, 1)

    def test_negative_id(self):
        """Using negative values to test"""
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

    def test_large_id(self):
        """Test with a large positive id value."""
        b1 = Base(10**9)
        self.assertEqual(b1.id, 10**9)

    def test_zero_id(self):
        """Test with id value of zero."""
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_none_id(self):
        """Test with id values as None."""
        b6 = Base(None)
        self.assertEqual(b6.id, 4)

    def test_assertRaise(self):
        """Test areas where TypeErrors might occur."""
        with self.assertRaises(TypeError):
            a = Base(1, 3, 4, 5)


if __name__ == "__main__":
    unittest.main()
