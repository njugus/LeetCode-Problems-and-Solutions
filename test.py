# return the number of  duplicate items in a list
num_list = [1, 2, 3, 5, 3]

def check_for_duplicates(my_array):
    num_dict = {}
    duplicates = []
    for num in my_array:  # 0(n)
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    for item in num_dict:  # 0(n)
        if num_dict[item] > 1:
            duplicates.append(item)
    return len(duplicates)


print(check_for_duplicates(num_list))
