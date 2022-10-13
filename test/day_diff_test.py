import unittest
from src.date_diff import date_diff, Date

class TestDateDiff(unittest.TestCase):

    def test_same(self):
        out = date_diff("01 01 1900, 01 01 1900")
        self.assertEqual(out, '01 01 1900, 01 01 1900, 0')

    def test_diff_1(self):
        out = date_diff("08 01 1995, 24 12 2005")
        self.assertEqual(out, '08 01 1995, 24 12 2005, 4003')

    def test_diff_2(self):
        out = date_diff("15 04 1969, 12 09 1945")
        self.assertEqual(out, '12 09 1945, 15 04 1969, 8616')

    def test_compare_day(self):
        d1 = Date(1, 1, 1900)
        d2 = Date(2, 1, 1900)

        self.assertTrue(d1 < d2)
        self.assertFalse(d1 > d2)

    def test_compare_month(self):
        d1 = Date(2, 1, 1900)
        d2 = Date(1, 2, 1900)

        self.assertFalse(d1 > d2)
        self.assertTrue(d1 < d2)

    def test_compare_year(self):
        d1 = Date(31, 1, 1900)
        d2 = Date(1, 1, 1901)

        self.assertFalse(d1 > d2)
        self.assertTrue(d1 < d2)

if __name__ == '__main__':
    unittest.main()