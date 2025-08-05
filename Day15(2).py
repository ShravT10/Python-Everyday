# # Difficulty: Easy
# # Description:
# # Given a string s containing only ()[]{},
# # determine if the input string is valid. A string is valid if:

# # Open brackets are closed by the same type of brackets.

# # Open brackets are closed in the correct order.

# Input: s = "()[]{}"
# Output: True

# Input: s = "(]"
# Output: False

def check_valid(s):
    ref = {"(":0,
           ")":0,
           "[":0,
           "]":0,
           "{":0,
           "}":0}
    
    for i in s:
        ref[i] = ref.get(i,0) + 1
    
    if ref["("] == ref[")"] and ref["["] == ref["]"] and ref["{"] == ref["}"]:
        return "Valid string"
    else:
        return "Invalid string"
    
print(check_valid("(){}[]"))