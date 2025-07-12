# Write a function single_digit_sum(n)
# that keeps summing the digits of a number until the result is a single digit.

# 📌 This is also known as the digital root.

# Example:

# Input: 942
# Step 1: 9 + 4 + 2 = 15
# Step 2: 1 + 5 = 6
# Output: 6

def single_digit_sum(s): #942

    while s>=10:
        s = sum(int(d) for d in str(s))
    return s
            
print(single_digit_sum(942))


