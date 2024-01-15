#!/usr/bin/python3
""" This module houses test cases for the base class """


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_creation_with_id(self):
        """
        Test if Base correctly assigns the provided id when an id is passed.
        """
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_creation_without_id(self):
        """
        Test if Base increments and assigns ids properly when created without
        providing an id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

    def test_mix_creation(self):
        """
        Test a combination of creating instances with and without ids,
        ensuring correct incrementation and assignment of ids.
        """
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        b4 = Base(20)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 20)

if __name__ == "__main__":
    unittest.main()
