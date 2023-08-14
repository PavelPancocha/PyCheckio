from unittest import TestCase

from home.changing_direction import changing_direction


class CountChangesTestCase(TestCase):

    def test_changing_direction_1(self):
        self.assertEqual(changing_direction([1, 2, 3, 4, 5]), 0)

    def test_changing_direction_2(self):
        self.assertEqual(changing_direction([1, 2, 3, 2, 1]), 1)

    def test_changing_direction_3(self):
        self.assertEqual(changing_direction([1, 2, 2, 1, 2, 2]), 2)
