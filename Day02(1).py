# Write a function count_vowels(s) that returns the number of vowels 
# (a, e, i, o, u) in a given string. Case-insensitive.

# Input: "Python Programming"
# Output: 4  # (o, o, a, i)

def count_vowels(s):
    vowels = "aeiou"
    list = [c for c in s if c in vowels]
    return len(list)

print(count_vowels("Python Programming"))

#GPT
#better

def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

# Test
print(count_vowels("Python Programming"))  # Output: 4
 
