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

    def test_mix_creation(self):
        """
        Test if Base increments and assigns ids properly when created without
        providing an id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual((b1.id, b2.id, b3.id, b4.id, b5.id), (1, 2, 3, 12, 4))


if __name__ == "__main__":
    unittest.main()
