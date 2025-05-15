#  find the first non-repeating character in a string
#  a character thats not been repeated in a word
from collections import Counter

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
