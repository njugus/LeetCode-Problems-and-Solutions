# Problem: Find the Maximum Sum of a Subarray of Size K
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# fixed size window

def max_sub_array(my_array, size):
    n = len(my_array)
    if n < size:
        return None

    window_sum = sum(my_array[:4])
    max_sum = window_sum

    for i in range(size, n):
        window_sum = window_sum + my_array[i] - my_array[i - size]
        max_sum = max(window_sum, max_sum)
    return max_sum


print(max_sub_array([2, 1, 5, 1, 3, 2], 4))