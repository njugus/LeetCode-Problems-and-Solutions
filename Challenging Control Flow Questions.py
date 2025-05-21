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
        print(f"Incorrect password. {3 - trial_count} attempts left.")
        continue
    elif password == real_password:
        print("Password Correct")

else:
    print("Account locked. Too many incorrect attempts.")


# a function that adds numbers in the same index between 2 lists
def get_sum_of_two_lists(list_1, list_2):
    if len(list_1) and len(list_2) == 0:
        return "The lists are empty"
    min_size = min(len(list_1), len(list_2))
    print(min_size)
    new_list = []
    for index in range(0, min_size):
        x = list_1[index] + list_2[index]
        new_list.append(x)

    return new_list


list_3 = []
list_4 = []
print(get_sum_of_two_lists(list_3, list_4))

# a function to find frequently repeated numbers in a list and return their frequency in a dictionary

my_array = [1, 2, 3, 2, 2, 4]


def count_repetitive_numbers(y):
    my_dict = {}
    for num in y:
        freq = my_array.count(num)
        my_dict[num] = freq

    return my_dict


print(count_repetitive_numbers(my_array))


# solve the 2 sum problem
def two_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    return []


result = two_sum([1, 2, 3, 4, 5, 8], 9)

if result:
    print(f"Pair found: {result}")
else:
    print("No pair found.")
