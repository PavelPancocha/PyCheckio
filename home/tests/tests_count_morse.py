from unittest import TestCase

from home.count_morse import count_morse


class TestCountMorse(TestCase):
    def test_count_morse_omg(self):
        self.assertEqual(count_morse("-------.", "omg"), 2)

    def test_count_morse_morse(self):
        self.assertEqual(count_morse(".....-.-----", "morse"), 4)

    def test_count_morse_xtmisuf(self):
        self.assertEqual(count_morse("-..----.......-..-.", "xtmisuf"), 4)

    def test_count_morse_when_etaoinshrdlu(self):
        self.assertEqual(count_morse(".-.----..-.........-.-...-....-", "etaoinshrdlu"), 122)
