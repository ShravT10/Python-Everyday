# # Statement:
# # Write a function is_palindrome(s) that checks if the string s is a palindrome 
# # (reads the same backward as forward). Ignore cases and spaces.

# Input: "A man a plan a canal Panama"
# Output: True

# name = "A man a plan a canal Panama"
name = input("Input a string : ")

def check(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(check(name))

 
