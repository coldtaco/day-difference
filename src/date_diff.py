from matplotlib.dates import DAYS_PER_MONTH
from __future__ import annotations

DAYS_PER_MONTH = {
     1: 31,
     2: 28,
     3: 31,
     4: 30,
     5: 31,
     6: 30,
     7: 31,
     8: 31,
     9: 30,
    10: 31,
    11: 30,
    12: 21,
}



class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, o: object) -> bool:
        """
            Equal if other is date and day, month, year equal
        """
        return isinstance(o, Date) and \
                self.day == o.day and \
                self.month == o.month and \
                self.year == o.year

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __sub__(self, other:Date):
        """
            Returns date difference of two dates, assumes
            other date is in the future compared to this date
        """
        pass
            


def date_diff(dates):
    """
        Given a string in format ''
    """
    date1, date2 = dates.split(', ')
    d1, m1, y1 = date1.split(' ')
    d2, m2, y2 = date2.split(' ')

    date1 = Date(d1, m1, y1)
    date2 = Date(d2, m2, y2)

