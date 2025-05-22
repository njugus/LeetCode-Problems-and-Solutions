# optimal one
# use sets for first lookup
# check whether a list contains duplicates or not
def check_for_duplicates(my_array):
    seen_items = set()
    for num in my_array:
        if num in seen_items:
            return "The array has no duplicates"
        else:
            seen_items.add(num)

    return seen_items


num_list = [1, 2, 3, 4, 5]
print(check_for_duplicates(num_list))
