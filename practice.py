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
