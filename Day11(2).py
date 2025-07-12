# Write a function common_elements(a, b, c) 
# that returns a list of elements that are common to all three lists.


# Input: [1, 2, 3], [2, 3, 4], [0, 2, 3, 5]
# Output: [2, 3]

def common_elements(a, b, c):
    return list(set(a) & set(b) & set(c))

# Test
print(common_elements([1, 2, 3], [2, 3, 4], [0, 2, 3, 5]))
# Output: [2, 3]
