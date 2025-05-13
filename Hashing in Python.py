# take the input convert it to a fixed-size value called a hash value through the hash function
# useful for fast lookups, insertion, deletion 0(1)
# dictionaries and sets do hashing internally
# Python’s set is just a hash table that stores only keys,
# and it uses hashing behind the scenes to do everything fast.

# example 1
grades = {"Kelvin": 97, "Lucy": 100, "Maryann": 99}
del grades["Lucy"]
print(grades)
print(grades["Kelvin"])

# Example 2
# using sets to store unique values
emails = ["a@mail.com", "b@mail.com", "a@mail.com"]
unique_emails = set(emails)
print(unique_emails)

# example 3
# count the number of occurrences of a value in an list
from collections import Counter
my_array = [1, 2, 3, 1, 2, 4, 5, 4]
num_frequency = Counter(my_array)
print(num_frequency)
print(type(num_frequency))


# example 4
# count the number of occurrences of a character in a string
my_name = "kelvin njuguna"
character_frequency = Counter(my_name)
print(character_frequency)
print(character_frequency.get('n'))

# example 5
# check whether two words are anagrams or not
from collections import Counter

def anagram_checker(x, y):
    return Counter(x) == Counter(y)


print(anagram_checker("post", "stop"))

