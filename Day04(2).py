# Type: Leetcode-style (Easy)
# Write a function are_anagrams(str1, str2) 
# that checks whether two strings are anagrams (same characters, different order).

# Ignore case and spaces.

# Example:

# python
# Copy
# Edit
# Input: "listen", "silent"
# Output: True

# def anagram(str1 , str2):
#     a = 0
#     for i in str1.replace(" ",""):
#         if i in str2.replace(" ",""):
#             a+=1
#     print(a)
    
#     if a == len(str1.replace(" ","")):
#         print(len(str1.replace(" ","")))
#         return True
#     else:
#         return False
    
# print(anagram("listen ","silent"))

def anagram(str1,str2):
    s1 = sorted(str1.replace(" ","").lower())
    s2 = sorted(str2.replace(" ","").lower())
    print(s1,s2)
    return s1 == s2

print(anagram("li sten ","sile nt"))