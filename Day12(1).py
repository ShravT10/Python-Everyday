# Write a function reverse_words(sentence)
# that reverses the order of words, not the letters.

# Input: "I love Python"
# Output: "Python love I"
# Solution:


def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Test
print(reverse_words("I love Python"))