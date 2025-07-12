# Type: String Logic
# Write a function is_rotation(s1, s2) 
# that checks if one string is a rotation of another.

# Input: "abcde", "cdeab"
# Output: True

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1

# Test
print(is_rotation("abcde", "cdeab"))  # Output: True
print(is_rotation("abc", "acb"))      # Output: False
