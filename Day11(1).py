# Write a function longest_word(sentence) that returns the longest word in the sentence.

# 📌 Ignore punctuation. You can assume words are separated by spaces.

# Input: "ChatGPT helps improve programming logic."
# Output: "programming"

import string

def longest_word(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    return max(words, key=len)

# Test
print(longest_word("ChatGPT helps improve programming logic."))
# Output: "programming"
