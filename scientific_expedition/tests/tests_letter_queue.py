import unittest
from unittest import TestCase

from scientific_expedition.letter_queue import letter_queue


class LetterQueueTestCase(TestCase):
    def test_1(self):
        self.assertEqual(letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]), "DOT")
        self.assertEqual(letter_queue(["POP", "POP"]), "")
        self.assertEqual(letter_queue(["PUSH H", "PUSH I"]), "HI")
        self.assertEqual(letter_queue([]), "")
