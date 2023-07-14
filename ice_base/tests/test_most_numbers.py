from unittest import TestCase

from ice_base.most_numbers import checkio


class MostNumbersTestCase(TestCase):
    def test_almost_equal_1(self):
        """Tests that checkio(1, 2, 3) equals 2."""
        self.assertAlmostEqual(checkio(1, 2, 3), 2, places=3)

    def test_almost_equal_2(self):
        """Tests that checkio(5, -5) equals 10."""
        self.assertAlmostEqual(checkio(5, -5), 10, places=3)

    def test_almost_equal_3(self):
        """Tests that checkio(10.2, -2.2, 0, 1.1, 0.5) equals 12.4."""
        self.assertAlmostEqual(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, places=3)

    def test_almost_equal_4(self):
        """Tests that checkio() equals 0."""
        self.assertAlmostEqual(checkio(), 0, places=3)
