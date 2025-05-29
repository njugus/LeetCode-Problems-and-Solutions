# reverse the entire string + reverse the words in the string

def reverse_words(s):
    words = s.strip().split()

    left = 0
    right = len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)


print(reverse_words("kelvin njuguna kagwima"))
