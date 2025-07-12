# Write a function remove_punctuation(s)
# that removes all punctuation characters from the input string.

# Hint: Use string.punctuation from the string module.

# Example:

# python
# Copy
# Edit
# Input: "Hello, World! How's it going?"
# Output: "Hello World Hows it going"
import string

S = "'!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"

def remove(s):
    return ''.join(c for c in s if c not in S)

print(remove("Hello, World! How's it going?"))

def remove1(s):
    return ''.join(c for c in s if c not in string.punctuation)

print(remove1("Hello, World! How's it going?"))