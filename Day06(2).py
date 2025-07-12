# Write a function find_pairs(lst, target)
# that returns all pairs of numbers from the list that add up to a given target sum.

# Example:

# python
# Copy
# Edit
# Input: [1, 2, 3, 4, 5], target = 6
# Output: [(1, 5), (2, 4)]

def fun(lst , target):
    seen = []
    pair = []
    for num in lst:
        diff = target - num
        if diff in seen:
            pair.append((diff,num))
        seen.append(num)
    print(pair)

fun([1,2,3,4,5],6)