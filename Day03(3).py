# Type: Competitive Programming
# Write a function count_frequency(lst) that counts 
# and returns the frequency of each element in a dictionary.

# Example:

# python
# Copy
# Edit
# Input: [1, 2, 2, 3, 3, 3]
# Output: {1: 1, 2: 2, 3: 3}

def freq(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i,0)+1
        print(freq)
    print(freq)

freq([1, 2, 2, 3, 3, 3])