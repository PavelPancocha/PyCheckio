from unittest import TestCase

from scientific_expedition.absolute_sorting import absolute_sort


class TestAbsolutSort(TestCase):
    def test_absolut_sort_case_1(self):
        self.assertEqual(absolute_sort([-20, -5, 10, 15]), [-5, 10, 15, -20])

    def test_absolut_sort_case_2(self):
        self.assertEqual(absolute_sort([1, 2, 3, 0]), [0, 1, 2, 3])

    def test_absolut_sort_case_3(self):
        self.assertEqual(absolute_sort([-1, -2, -3, 0]), [0, -1, -2, -3])
