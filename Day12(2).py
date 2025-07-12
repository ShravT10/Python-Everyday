# A perfect number is one that is equal to the sum of its proper divisors (excluding itself).
# Write a function is_perfect(n) that checks if n is a perfect number.

# Input: 28 → Divisors: 1 + 2 + 4 + 7 + 14 = 28
# Output: True

def is_perfect(n):
    r = 0
    for i in range(1,n):
        if n % i == 0:
            r += i
    return r==n

print(is_perfect(28))