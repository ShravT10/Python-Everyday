# Type: Leetcode-style (Easy)
# Write a function remove_duplicates(lst)
# that removes duplicates from a list while preserving the original order.

# Example:

# python
# Copy
# Edit
# Input: [1, 2, 2, 3, 1, 4]
# Output: [1, 2, 3, 4]

def red(s):
    a = []
    for c in s:
        if c not in a:
            a.append(c)
            print(c)
    return a

print(red([1, 2, 2, 3, 1, 4,3,9,8,6,9,1,2,3,5,6,7,0,7,3,4,6,5,0]))

#gpt

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test
print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # Output: [1, 2, 3, 4]
