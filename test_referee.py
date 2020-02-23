from unittest import TestCase
from referee import checkio as referee


class TestReferee(TestCase):
    def test_X_win_horizontal(self):
        self.assertEqual(referee([
            "XXX",
            "OO.",
            "XOO"]), "X")

    def test_draw(self):
        self.assertEqual(referee([
            "OOX",
            "XXO",
            "OXX"]), "D")

    def test_O_win_vertical(self):
        self.assertEqual(referee([
             "OO.",
             "XOX",
             "XOX"]), "O")

    def test_X_win_diagonal(self):
        self.assertEqual(referee([
            "X.X",
            "OX.",
            "XOO"]), "X")