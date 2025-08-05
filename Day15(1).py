# # Description:
# # Given an array of integers nums and 
# # an integer target, return indices of the two numbers such that they add up to target.

# # Return the answer in any order. 
# # You may assume exactly one solution exists, and you may not use the same element twice.

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

def two_sum(lst,tar):
    check = [] #[ 7 , 2 , -2 , -6]
    for i in lst:
        diff = tar - i
        check.append(diff)
    for j in lst:
        jiff = tar - j
        if jiff in check:
            return[j,jiff]
    
    
print(two_sum([3, 7, 11, 15],10))
