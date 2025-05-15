# example using ordered dict
# anytime you want to preserve the order of items in a dict and perform an operations
# e.g find their frequencies then use ordered dict

from collections import OrderedDict


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