def leapyears(yearlist):
    """Returns a generator that returns the leap years in yearlist

    >>> years = [1600, 1604, 1700, 1704, 1800, 1900, 1996, 2000, 2004]
    >>> list(leapyears(years))
    [1600, 1604, 1704, 1996, 2000, 2004]
    """
    for year in yearlist:
        if year % 4 == 0:
            if year % 100 == 0 and not year % 400 == 0:
                continue
            yield year