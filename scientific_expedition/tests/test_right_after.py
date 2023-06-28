from unittest import TestCase

from scientific_expedition.right_after import goes_after


class TestRightAfter(TestCase):

    def test_goes_after_case_2(self):
        self.assertIs(goes_after("world", "w", "r"), False)

    def test_goes_after_case_3(self):
        self.assertIs(goes_after("world", "l", "o"), False)

    def test_goes_after_case_4(self):
        self.assertIs(goes_after("panorama", "a", "n"), True)

    def test_goes_after_case_5(self):
        self.assertIs(goes_after("list", "l", "o"), False)

    def test_goes_after_case_6(self):
        self.assertIs(goes_after("", "l", "o"), False)

    def test_goes_after_case_7(self):
        self.assertIs(goes_after("list", "l", "l"), False)

    def test_goes_after_case_8(self):
        self.assertIs(goes_after("world", "d", "w"), False)

    def test_goes_after_case_9(self):
        self.assertIs(goes_after("Almaz", "a", "l"), False)

    def test_goes_after_case_10(self):
        self.assertIs(goes_after('transport', 'r', 't'), False)
        
    def test_goes_after_case_11(self):
        self.assertIs(goes_after('almaz', 'm', 'a'), False)
