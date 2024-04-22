"""This moodule houses test cases for the square class"""

from io import StringIO
import sys
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """This contains all test cases for the Square class."""
    def test_instantiation(self):
        """Check to see if initialized well."""
        r1 = Square(5)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(str(r1), "[Square] (7) 0/0 - 5")

        s2 = Square(2, 2)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 8)

    def test_display(self):
        """
        Test the display() method
        """
        s1 = Square(5)
        captured = StringIO()
        sys.stdout = captured
        s1.display()

        expected = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(captured.getvalue(), expected)

        captured.truncate(0)
        captured.seek(0)

        sys.stdout = sys.__stdout__

        s2 = Square(2, 2)
        captured = StringIO()
        sys.stdout = captured
        s2.display()

        expected_output = "  ##\n  ##\n"
        self.assertEqual(captured.getvalue(), expected_output)

        captured.truncate(0)
        captured.seek(0)

        sys.stdout = sys.__stdout__

        s3 = Square(3, 1, 3)
        expected_value = "\n\n\n ###\n ###\n ###\n"

        captured = StringIO()
        sys.stdout = captured
        s3.display()

        self.assertEqual(captured.getvalue(), expected_value)

        sys.stdout = sys.__stdout__

    def test_area(self):
        """Test the area method of the Square class."""
        a = Square(5)
        self.assertEqual(a.area(), 25)

        b = Square(10)
        self.assertEqual(b.area(), 100)

        s3 = Square(3, 1, 1)
        self.assertEqual(s3.area(), 9)

    def test_square_inheritance(self):
        """Test the inheritance of the Square class"""
        s1 = Square(6)
        self.assertTrue(isinstance(s1, Square))
        self.assertTrue(isinstance(s1, Rectangle))

    def test_square_size_getter(self):
        """Test case to ensure the size setter works correctly."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(5)
        s2.size = 10
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)

    def test_square_setter_invalid(self):
        """Test case to ensure size setters handle invalid input."""
        s1 = Square(5)

        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_square_update_method_args(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)

    def test_square_update_method_args_multiple(self):
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_square_update_method_kwargs(self):
        s1 = Square(5)
        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)

    def test_upgrade_method(self):
        """ test cases to test the upgrade method of the Square class."""
        from models.square import Square
        s1 = Square(5)
        s1.update(z=13)

        exp = {
            '_Rectangle__width': 5,
            '_Rectangle__height': 5,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0,
            'id': 16
            }
        self.assertEqual(s1.__dict__, exp)

    def test_to_dictionary_method(self):
        """Test case for to_dictionary() method."""
        z = Square(10, 2, 1)
        self.assertEqual(str(z), "[Square] (17) 2/1 - 10")
        expected = {
            'id': 17,
            'x': 2,
            'size': 10,
            'y': 1
            }
        self.assertEqual(z.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
