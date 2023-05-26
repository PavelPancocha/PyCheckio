from unittest import TestCase

from home.electronic_station.words_order import words_order


class WordsOrderTestCase(TestCase):
    def test_case_1(self):
        self.assertTrue(words_order("hi world im here", ["world", "here"]))

    def test_case_2(self):
        self.assertFalse(words_order("hi world im here", ["here", "world"]))

    def test_case_3(self):
        self.assertTrue(words_order("hi world im here", ["world"]))

    def test_case_4(self):
        self.assertFalse(words_order("hi world im here", ["world", "here", "hi"]))

    def test_case_5(self):
        self.assertTrue(words_order("hi world im here", ["world", "im", "here"]))

    def test_case_6(self):
        self.assertFalse(words_order("hi world im here", ["world", "hi", "here"]))

    def test_case_7(self):
        self.assertFalse(words_order("hi world im here", ["world", "world"]))

    def test_case_8(self):
        self.assertFalse(words_order("hi world im here", ["country", "world"]))

    def test_case_9(self):
        self.assertFalse(words_order("hi world im here", ["wo", "rld"]))

    def test_case_10(self):
        self.assertFalse(words_order("", ["world", "here"]))

    def test_case_11(self):
        self.assertFalse(words_order("hi world world im here", ["world", "world"]))

    def test_case_12(self):
        self.assertTrue(words_order("hi world world im here hi world world im here", ["world", "here"]))

