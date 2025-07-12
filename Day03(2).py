# Write a function second_largest(lst) 
# that returns the second largest number in a list.

# Example:

# python
# Copy
# Edit
# Input: [10, 20, 4, 45, 99]
# Output: 45

def second_lar(s):
    frst = 0
    for c in s: 
        if c > frst:
            frst = c
    # print(frst)

    s.remove(frst)
    # print(s)
    s1 = 0
    for c in s: 
        if c > s1:
            s1 = c
    
    print(s1)

second_lar([10, 20, 4, 45])

# gpt

# def second_largest(lst):
#     unique_nums = list(set(lst)) #set removes duplicate value , list converts the set back to a list
#     if len(unique_nums) < 2:
#         return None  # No second largest
#     unique_nums.sort()
#     return unique_nums[-2]

# print(second_largest([10, 20, 4, 45]))