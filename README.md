# Date diff

`date_diff.py/date_diff`
Given a string in format `DD MM YYYY, DD MM YYYY`
returns a string in format `DD MM YYYY, DD MM YYYY, {day diff}`
where day diff is the number of days between the dates (positive integer)

Return string will place the earlier date before the later date
therefore order of dates maybe be swapped
```
Input> 08 01 1995, 24 12 2005
Output> 08 01 1995, 24 12 2005, 4003

Input> 15 04 1969, 12 09 1945
Output> 12 09 1945, 15 04 1969, 861
```

`date_diff.py/Date`
Date object that allows for comparing two date objects
Also allows taking the difference between dates to return number of days between them
Returns negative date if `date1` is later than `date2` given `date1 - date2`