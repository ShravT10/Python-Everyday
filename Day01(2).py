# Statement:
# Given a list containing n distinct numbers taken from the range 0 to n, 
# find the one number that is missing from the list.

# Input: [3, 0, 1]
# Output: 2

def miss(*args):
    for i in range(0,len(args)):
        if i in args:
            pass
        else:
            print(i)

miss(3,0,1,4)



def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

# Test
print(missing_number([3, 0, 2,4]))  # Output: 2
 
