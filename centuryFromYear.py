def centuryFromYear(year):
    if year%100 > 0:
        year += 100
        year = year - year%100
    year = year/100
    return year
