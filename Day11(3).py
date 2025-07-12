# Write a recursive function reverse_string(s) that returns the reverse of the string.

# Input: "hello"
# Output: "olleh"

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# Test
print(reverse_string("hello"))  # Output: "olleh"