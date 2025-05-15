# take the input convert it to a fixed-size value called a hash value through the hash function
# useful for fast lookups, insertion, deletion 0(1)
# dictionaries and sets do hashing internally
# Python’s set is just a hash table that stores only keys,
# and it uses hashing behind the scenes to do everything fast.

from collections import OrderedDict
from collections import Counter

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


def anagram_checker(x, y):
    return Counter(x) == Counter(y)


print(anagram_checker("post", "stop"))

#  find the first non-repeating character in a string
#  a character thats not been repeated in a word

input_word = str(input("Enter a word: "))


# input string validator
def string_validator():
    new_string = " ".join(char.lower() for char in input_word if char.isalnum())
    if not new_string:
        return "Invalid characters in the string"
    return new_string


# processing
def no_repeating_char():
    cleaned_string = string_validator()
    char_freq = Counter(cleaned_string)
    for key in char_freq:
        if char_freq[key] == 1:
            return key

    return "all characters are repeated"


print(no_repeating_char())



# example using ordered dict
# anytime you want to preserve the order of items in a dict and perform an operations
# e.g find their frequencies then use ordered dict

def find_non_repeating_char():
    char_count = OrderedDict()
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count == 1:
            return char
    return "all characters have been repeated"


word = str(input("Enter a word: "))
print(find_non_repeating_char())