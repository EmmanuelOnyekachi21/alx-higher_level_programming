"""This moodule houses test cases for the square class"""



import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def test_instantiation(self):
        r1 = Square(5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(str(r1), "[Square] (1) 0/0 - 5")
        self.assertEqual(r1.area(), 25)

    def test_square_inheritance(self):
        s1 = Square(6)
        self.assertTrue(isinstance(s1, Square))
        self.assertTrue(isinstance(s1, Rectangle))

    def test_square_size_getter(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_square_size_setter(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

    def test_square_setter_invalid(self):
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

    def test_square_upodate_method_kwargs(self):
        s1 = Square(5)
        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)


if __name__ == "__main__":
    unittest.main()
