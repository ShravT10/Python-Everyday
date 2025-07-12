# # Write a function is_anagram(s1, s2) 
# # that checks if two strings are anagrams (case-insensitive and ignoring spaces).

# # 📌 An anagram is a rearrangement of letters forming another word.

# Input: "Listen", "Silent"
# Output: True

# Input: "School master", "The classroom"
# Output: True

def isAnagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    return sorted(s1) == sorted(s2)

print(isAnagram("Listen", "Silent"))