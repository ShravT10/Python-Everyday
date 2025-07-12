# Write a function is_pangram(s) 
# that checks whether a sentence contains every letter of the English alphabet at least once.

# Ignore case and spaces.

# Example:

# python
# Copy
# Edit
# Input: "The quick brown fox jumps over the lazy dog"
# Output: True

def checkPangram(s):
    ref = "abcdefghijklmnopqrstuvwxyz"
    num = 0
    for _ in s:
        if _.lower() in ref:
            ref.replace(_,"")
            num = num + 1
    
    if num>=26:
        print("The sentence is a Pangram")
    else:
        print("not a Pangram")

s = input("Enter your Sentence : ")
checkPangram(s)