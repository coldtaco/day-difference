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

    def __lt__(self, other:Date):
        if self.year > other.year:
            return False
        elif self.year < other.year:
            return True
        # Same year
        if self.month > other.month:
            return False
        elif self.month < other.month:
            return True
        # Same month
        return self.day < other.day

    def __sub__(self, other:Date) -> int:
        """
            Returns date difference of two dates
        """
        # Assume other is larger than self
        # Move self closer to other
        if self > other:
            return - (other - self)
        other = other.__copy__() # Make copy so operations dont override

        day_diff = other.day - self.day

        while other.year - self.year > 4:
            # Day difference for 4 years, include leap year
            day_diff += 365*3 + 366
            self.year += 4

        # Difference is less than 4 years, check if years are leap
        while self.year < other.year:
            leap_year = Date.is_leap_year(self.year)
            if leap_year:
                day_diff += 366
            else:
                day_diff += 365
            self.year += 1

        while self.month < other.month:
            if self.month == 2 and Date.is_leap_year(self.year):
                day_diff += 29
            else:
                day_diff += DAYS_PER_MONTH[self.month]

            self.month += 1
        
        return - day_diff
        

    @staticmethod
    def is_leap_year(year):
        if year % 400:
            return True
        # Only century year
        elif year % 100:
            return False
        # Leap year
        elif year % 4:
            return True
        # Non leap year
        else:
            return False


    def __repr__(self) -> str:
        return f'{self.day} {self.month} {self.year}'
            


def date_diff(dates):
    """
        Given a string in format ''
    """
    date1, date2 = dates.split(', ')
    d1, m1, y1 = date1.split(' ')
    d2, m2, y2 = date2.split(' ')

    date1 = Date(d1, m1, y1)
    date2 = Date(d2, m2, y2)

