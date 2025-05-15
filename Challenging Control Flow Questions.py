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

# Password Checker
# Ask the user for a password. Let them try up to 3 times.
# Lock them out after 3 wrong tries.

real_password = "tania"
trial_count = 0

while trial_count < 3:
    password = str(input("Enter a password: "))
    if password != real_password:
        trial_count += 1
        continue

    print("Password correct!!")
    break

