# Given a sorted array of integers and a target sum, return the indices (1-based or 0-based) of
# the two numbers that add up to the target.
# using pointers and then moving those pointers based on conditions

arr = [2, 4, 7, 11, 15]


def two_sum_sorted(my_array, target):
    left = 0
    right = len(my_array) - 1

    while left < right:
        sum = my_array[left] + my_array[right]
        if sum == target:
            return left, right
        elif sum > target:
            right -= 1
        else:
            left += 1

    return None


print(two_sum_sorted(arr, 45))


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