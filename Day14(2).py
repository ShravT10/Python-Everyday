# # Write a function is_palindrome(s) 
# # that returns True if the string is a palindrome, ignoring case and spaces

# Input: "A man a plan a canal Panama"
# Output: True


def is_palindrome(s):
    res = ''.join(c.lower() for c in s if c.isalnum())
    return res == res[::-1]

print(is_palindrome("A man a plan a canal Panama"))