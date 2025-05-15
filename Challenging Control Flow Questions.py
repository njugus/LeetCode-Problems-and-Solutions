# check whether a year is leap or not
year = int(input("Enter a year: "))


# processing
def leap_year_checker():
    if year % 400 == 0 and year % 100 == 0:
        return "Year is a leap year"
    elif year % 4 == 0 and year % 100 != 0:
        return "Year is a leap year"
    return "Year is not a leap year"


print(leap_year_checker())
