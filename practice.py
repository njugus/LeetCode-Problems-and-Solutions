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




