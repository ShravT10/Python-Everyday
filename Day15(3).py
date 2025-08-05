# Given an array nums, write a 
# function to move all 0's to the end while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.

# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


def move_zero(lst1):
    lst = lst1
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.pop(i)
            lst.append(0)
    return lst

print(move_zero([0, 1, 0, 3, 12]))


