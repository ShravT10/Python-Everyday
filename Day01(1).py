# Type: Logic Building
# Statement:
# Write a Python function sum_of_digits(n) that returns the sum of the digits of a number n.

def add(n):
    print(sum(int(n) for n in str(n) ))

yay = int(input("Enter your number : "))
add(yay)

