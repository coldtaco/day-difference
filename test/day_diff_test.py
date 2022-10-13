import unittest
from src.date_diff import date_diff, Date

class TestDateDiff(unittest.TestCase):

    def test_diff_date_simple(self):
        """
            Simple date difference check
        """
        d1 = Date(1, 1, 1900)
        d2 = Date(2, 1, 1900)

        self.assertEqual(d1 - d2, -1)
        self.assertEqual(d2 - d1, 1)

    def test_diff_date_simple_month(self):
        """
            Check day diff for one month
        """
        d1 = Date(1, 1, 1900)
        d2 = Date(1, 2, 1900)
        self.assertEqual(d2 - d1, 31)

    def test_leap_year(self):
        """
            Check one leap year
        """
        d1 = Date(1, 5, 1900)
        d2 = Date(1, 5, 1904)
        self.assertEqual(d2 - d1, 365 * 3 + 366)

    def test_leap_year_2(self):
        """
            No leap year for 1900 (one leap year)
        """
        d1 = Date(1, 1, 1900)
        d2 = Date(1, 1, 1905)
        self.assertEqual(d2 - d1, 365 * 4 + 366*1)

    def test_leap_year_2(self):
        """
            Two leap years
        """
        d1 = Date(1, 1, 1904)
        d2 = Date(1, 1, 1909)
        self.assertEqual(d2 - d1, 365 * 3 + 366*2)

    def test_day_month(self):
        """
            Check date diff works for all days, months
        """
        d1 = Date(1, 1, 1900)
        d2 = Date(31, 12, 1900)
        self.assertEqual(d2 - d1, 364)

    def test_m_d_larger(self):
        """
            Take difference in dates, month day are both larger,
            one year difference (test negative month, day checking)
        """
        d1 = Date(31, 12, 1900)
        d2 = Date(1, 1, 1901)
        self.assertEqual(d2 - d1, 1)

    def test_year_diff(self):
        """
            Take difference in year (non leap year)
        """
        d1 = Date(1, 5, 1900)
        d2 = Date(1, 5, 1901)
        self.assertEqual(d2 - d1, 365)

    def test_same(self):
        """
            Test same date
        """
        out = date_diff("01 01 1900, 01 01 1900")
        self.assertEqual(out, '01 01 1900, 01 01 1900, 0')

    def test_diff_1(self):
        """
            Provided test 1, normal date order
        """
        out = date_diff("08 01 1995, 24 12 2005")
        self.assertEqual(out, '08 01 1995, 24 12 2005, 4003')

    def test_diff_2(self):
        """
            Provided test 2, reverse date order
        """
        out = date_diff("15 04 1969, 12 09 1945")
        self.assertEqual(out, '12 09 1945, 15 04 1969, 8616')

    def test_compare_day(self):
        """
            Test comparing dates when days are different
        """
        d1 = Date(1, 1, 1900)
        d2 = Date(2, 1, 1900)

        self.assertTrue(d1 < d2)
        self.assertFalse(d1 > d2)

    def test_compare_month(self):
        """
            Test comparing dates when months are different
        """
        d1 = Date(2, 1, 1900)
        d2 = Date(1, 2, 1900)

        self.assertFalse(d1 > d2)
        self.assertTrue(d1 < d2)

    def test_compare_year(self):
        """
            Test comparing dates when years are different
        """
        d1 = Date(31, 1, 1900)
        d2 = Date(1, 1, 1901)

        self.assertFalse(d1 > d2)
        self.assertTrue(d1 < d2)

    def test_compare_equal(self):
        """
            Test comparing dates are equal
        """
        d1 = Date(1, 1, 1900)
        d2 = Date(1, 1, 1900)

        self.assertFalse(d1 > d2)
        self.assertFalse(d1 < d2)
        self.assertEqual(d1, d2)

if __name__ == '__main__':
    unittest.main()