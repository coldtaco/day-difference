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
    """
        Date class, allows for computing day difference between two dates
    """
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
            Returns day difference of two dates
            returns negative day if other is smaller
        """
        # Assume other is larger than self
        # Move self closer to other
        if self > other:
            return - (other - self)
        self_cpy = self.__copy__() # Make copy so operations dont override

        # Total day difference between dates, start from days
        day_diff = other.day - self_cpy.day

        # Move self month closer to other month to the right (future)
        while self_cpy.month < other.month:
            if self_cpy.month == 2 and Date.is_leap_year(self_cpy.year):
                day_diff += 29
            else:
                day_diff += DAYS_PER_MONTH[self_cpy.month]

            self_cpy.month += 1

        # Move self month closer to other month to the left (past)
        while self_cpy.month > other.month:
            self_cpy.month -= 1

            if self_cpy.month == 2 and Date.is_leap_year(self_cpy.year):
                day_diff -= 29
            else:
                day_diff -= DAYS_PER_MONTH[self_cpy.month]

        # Note: No need to check for past year like we did for month
        # because year is guarenteed to be <= other year from check at the start

        # Move self year to other year to the right (future)
        while self_cpy.year < other.year:
            if self_cpy.month <= 2:
                leap_year = Date.is_leap_year(self_cpy.year)
            else:
                leap_year = Date.is_leap_year(self_cpy.year + 1)
            if leap_year:
                day_diff += 366
            else:
                day_diff += 365
            self_cpy.year += 1
        
        return - day_diff

    @staticmethod
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        # Only century year
        elif year % 100 == 0:
            return False
        # Leap year
        elif year % 4 == 0:
            return True
        # Non leap year
        else:
            return False

    def __repr__(self) -> str:
        return f'{self.day:02} {self.month:02} {self.year:04}'


def date_diff(dates):
    """
        Given a string in format 'DD MM YYYY, DD MM YYYY'
        returns a string in format 'DD MM YYYY, DD MM YYYY, {day diff}'
        where day diff is the number of days between the dates (positive integer)

        Return string will place the earlier date before the later date
        therefore order of dates maybe be swapped
    """
    date1, date2 = dates.split(', ')

    # Split date into day, month, year, convert all to int
    d1, m1, y1 = [int(i) for i in date1.split(' ')]
    d2, m2, y2 = [int(i) for i in date2.split(' ')]

    date1 = Date(d1, m1, y1)
    date2 = Date(d2, m2, y2)

    if date2 < date1:
        date2, date1 = date1, date2

    diff = date2 - date1

    return f'{date1}, {date2}, {diff}'
