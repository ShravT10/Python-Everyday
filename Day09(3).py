# Write a function group_by_first_letter(words) 
# that groups a list of words into a dictionary, 
# where each key is the first letter.

# Input: ["apple", "banana", "apricot", "blueberry", "cherry"]
# Output:
# {
#   'a': ['apple', 'apricot'],
#   'b': ['banana', 'blueberry'],
#   'c': ['cherry']
# }

def group_by_first_letter(words): #WEEEEEEEEEEEEEEEEEEEEE
    grouped = {}
    for i in words:
        key = i[0]
        grouped.setdefault(key , []).append(i)
    print(grouped)

print(group_by_first_letter(["apple", "banana", "apricot", "blueberry", "cherry"]))