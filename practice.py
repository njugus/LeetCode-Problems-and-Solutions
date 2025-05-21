# solve the 2 sum problem
def two_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    return []


result = two_sum([1, 2, 3, 4, 5, 8], 9)

if result:
    print(f"Pair found: {result}")
else:
    print("No pair found.")
