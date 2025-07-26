# # Type: Sliding Window (Popular in Interviews)
# # Write a function max_sum_subarray(arr, k)
# # that returns the maximum sum of any contiguous subarray of size k.

# Input: arr = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9  (subarray: [5, 1, 3])

def max_sum_subarray(arr, k):
    max_sum = 0
    for i in range(0, len(arr) - k + 1):
        current_sum = sum(arr[i:i+k])  # compute subarray sum
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
