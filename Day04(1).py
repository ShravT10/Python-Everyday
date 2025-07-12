# Write a function squares_of_even(nums) 4
#that returns a list of squares of all even numbers from the input list.

# Example:

# python
# Copy
# Edit
# Input: [1, 2, 3, 4, 5]
# Output: [4, 16]

def square_of_even(m):
    s=[]
    for i in m:
        if i%2==0:
            s.append(i*i)
    return s
        

print(square_of_even([1, 2, 3, 4, 5 , 6]))

def square_of_even(m):
    return [x*x for x in m if x%2==0]

print(square_of_even([1, 2, 3, 4, 5 , 6]))