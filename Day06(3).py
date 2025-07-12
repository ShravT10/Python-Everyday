# Type: Competitive Programming
# Write a function gcd(a, b)
# that returns the greatest common divisor of two numbers using the Euclidean algorithm.

# Example:

# python
# Copy
# Edit
# Input: 60, 48
# Output: 12

def hmph(a,b):
    cd = []
    for i in range(1,a+1):
        if a%i==0:
            if b%i==0:
                cd.append(i)

    print("Highest Common Divisor : ",cd[-1]) 

def zzz(a,b):
    if a>b:
        hmph(a,b)
    else:
        hmph(b,a)

a = int(input("Input 1st number : "))
b = int(input("Input 2nd number : "))
zzz(a,b)