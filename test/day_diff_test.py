import unittest
from src.date_diff import date_diff

class TestDateDiff(unittest.TestCase):

    def test_same(self):
        out = date_diff("01 01 1900, 01 01 1900")
        self.assertEqual(out == '01 01 1900, 01 01 1900, 0')

    def test_diff_1(self):
        out = date_diff("08 01 1995, 24 12 2005")
        self.assertEqual(out == '08 01 1995, 24 12 2005, 4003')

    def test_diff_2(self):
        out = date_diff("15 04 1969, 12 09 1945")
        self.assertEqual(out == '12 09 1945, 15 04 1969, 8616')