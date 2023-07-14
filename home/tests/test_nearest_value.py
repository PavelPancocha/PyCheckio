from unittest import TestCase

from home.nearest_value import nearest_value


class TestNearestValue(TestCase):
    def test_nearest_value_1(self):
        self.assertEqual(nearest_value({17, 4, 7, 10, 11, 12}, 9), 10)

    def test_nearest_value_2(self):
        self.assertEqual(nearest_value({17, 4, 7, 10, 11, 12}, 8), 7)

    def test_nearest_value_3(self):
        self.assertEqual(nearest_value({17, 4, 8, 10, 11, 12}, 9), 8)

    def test_nearest_value_4(self):
        self.assertEqual(nearest_value({17, 4, 9, 10, 11, 12}, 9), 9)

    def test_nearest_value_5(self):
        self.assertEqual(nearest_value({17, 4, 7, 10, 11, 12}, 0), 4)

    def test_nearest_value_6(self):
        self.assertEqual(nearest_value({17, 4, 7, 10, 11, 12}, 100), 17)

    def test_nearest_value_7(self):
        self.assertEqual(nearest_value({100, 5, 8, 89, 10, 12}, 7), 8)

    def test_nearest_value_8(self):
        self.assertEqual(nearest_value({2, 3, -1}, 0), -1)

    def test_nearest_value_9(self):
        self.assertEqual(nearest_value({5}, 5), 5)

    def test_nearest_value_10(self):
        self.assertEqual(nearest_value({0, -2}, -1), -2)
