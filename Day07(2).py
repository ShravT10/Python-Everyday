# Write a function majority_element(nums)
# that returns the element that appears more than n/2 times in the list.
# You can assume such an element always exists.

# Example:
# python

# Input: [2, 2, 1, 1, 2, 2, 2]
# Output: 2

def majority(num):
    checked = {}
    for i in num:
        checked[i] = checked.get(i,0)+1
        
    return max(checked, key=checked.get)

    
print(majority([2, 2, 1, 1, 2, 2, 2,1,1,1,1,1,1,1]))