from unittest import TestCase

from ice_base.count_chains import count_chains


class CountChainsTestCase(TestCase):

    def test_count_chains_1(self):
        self.assertEqual(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]), 2)

    def test_count_chains_2(self):
        self.assertEqual(count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]), 1)

    def test_count_chains_3(self):
        self.assertEqual(count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]), 1)

    def test_count_chains_4(self):
        self.assertEqual(count_chains([(2, 2, 1), (2, 2, 2)]), 2)

    def test_count_chains_5(self):
        self.assertEqual(count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]), 4)

    def test_count_chains_6(self):
         self.assertEqual(count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]), 2)

    def test_count_chains_7(self):
        self.assertEqual(count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]), 1)
