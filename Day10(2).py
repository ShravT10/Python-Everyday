# Write a function product_except_self(nums) 
# that returns a list where each element is the product of all other elements except itself.

# Without using division.


# Input: [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

def product_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [0] * n

    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    for i in range(n):
        result[i] = left[i] * right[i]

    return result

# Test
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
