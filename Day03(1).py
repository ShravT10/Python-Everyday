# Type: Logic Building
# Write a function reverse_words(s) that takes a sentence
# and returns a new sentence with the words reversed, not the characters.

# Example:

# python
# Copy
# Edit
# Input: "Hello World from Python"
# Output: "Python from World Hello"

def reverse_words(s):
    ss = s.split()
    print(ss)
    r = ' '.join(reversed(ss))
    print(r)  
    
reverse_words("Hello ji")

