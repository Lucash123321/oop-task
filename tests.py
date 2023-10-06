import unittest
from main import Circle, Triangle
import math


class TestTriangle(unittest.TestCase):

    def test_triangle_does_not_exist(self):
        self.assertRaises(ValueError, Triangle, 1, 2, 99)
        self.assertRaises(ValueError, Triangle, -1, 2, 99)

    def test_square(self):
        triangle = Triangle(13, 14, 15)
        self.assertEqual(84, triangle.square())

        triangle = Triangle(3, 4, 5)
        self.assertEqual(6, triangle.square())

    def test_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(True, triangle.is_right())

        triangle = Triangle(10, 12, 15)
        self.assertEqual(False, triangle.is_right())


class TestCircle(unittest.TestCase):

    def test_circle_does_not_exist(self):
        self.assertRaises(ValueError, Circle, -1)

    def test_square(self):
        circle = Circle(4)
        self.assertEqual(16 * math.pi, circle.square())

        circle = Circle(10)
        self.assertEqual(100 * math.pi, circle.square())
