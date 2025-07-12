# Type: Leetcode-style
# Write a function rotate_list(lst, k)
# that rotates the list to the right by k steps.

# Example:

# python
# Copy
# Edit
# Input: [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate(lst , a):
    a = a % len(lst)
    return lst[-a:] + lst[:-a]

print(rotate([1, 2, 3, 4, 5],2))