from unittest import TestCase

from github.expand_intervals import expand_intervals


class TestExpandIntervals(TestCase):
    def test_expand_intervals_case1(self):
        self.assertEqual(list(expand_intervals([(1, 3), (5, 7)])), [1, 2, 3, 5, 6, 7])

    def test_expand_intervals_case2(self):
        self.assertEqual(list(expand_intervals([(1, 3)])), [1, 2, 3])

    def test_expand_intervals_case3(self):
        self.assertEqual(list(expand_intervals([])), [])

    def test_expand_intervals_case4(self):
        self.assertEqual(list(expand_intervals([(1, 2), (4, 4)])), [1, 2, 4])
