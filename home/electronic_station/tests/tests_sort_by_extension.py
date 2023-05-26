from unittest import TestCase

from home.electronic_station.sort_by_extension import sort_by_ext


class TestSortByExt(TestCase):
    def test_case1(self):
        self.assertEqual(sort_by_ext(["1.cad", "1.bat", "1.aa"]), ["1.aa", "1.bat", "1.cad"])

    def test_case2(self):
        self.assertEqual(sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]),
                         ["1.aa", "1.bat", "2.bat", "1.cad"])

    def test_case3(self):
        self.assertEqual(sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]),
                         [".bat", "1.aa", "1.bat", "1.cad"])

    def test_case4(self):
        self.assertEqual(sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]),
                         [".aa", ".bat", "1.bat", "1.cad"])

    def test_case5(self):
        self.assertEqual(sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']), ['1.aa', '1.bat', '1.cad', '.aa.doc'])
