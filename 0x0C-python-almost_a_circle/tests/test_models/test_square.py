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


if __name__ == "__main__":
    unittest.main()
