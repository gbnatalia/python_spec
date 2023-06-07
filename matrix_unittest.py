import unittest
from matrix import *

class TestCaseMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.m3 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        self.m4 = Matrix([[1, 2], [4, 5], [7, 8]])

    def test_equal(self):
        self.assertEqual(self.m1 == self.m2, True, "Ошибка!")
        self.assertEqual(self.m1 == self.m3, False, "Ошибка!")

    def test_not_equal(self):
        self.assertEqual(self.m1 != self.m2, False, "Ошибка!")
        self.assertEqual(self.m1 != self.m3, True, "Ошибка!")

    def test_lt(self):
        self.assertEqual(self.m1 < self.m2,  False, "Ошибка!")

    def test_le(self):
        self.assertEqual(self.m1 <= self.m2, True, "Ошибка!")

    def test_gt(self):
        self.assertEqual(self.m1 > self.m2, False, "Ошибка!")

    def test_ge(self):
        self.assertEqual(self.m1 >= self.m2, True, "Ошибка!")

    def test_add(self):
        self.assertEqual(self.m1+self.m2, Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), "Ошибка")

    def test_transport(self):
        self.assertEqual(self.m4.transpose(), Matrix([[1, 4, 7], [2, 5, 8]]), "Ошибка")

    def test_init(self):
        with self.assertRaises(MatrixTypeDataError):
            Matrix([[]])

    def test_size(self):
        with self.assertRaises(MatrixSizeError):
            self.m1 + self.m4


if __name__=="__main__":
    unittest.main()
