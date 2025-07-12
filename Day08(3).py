# Write a function merge_alternate(list1, list2)
# that returns a new list by picking elements alternately from both lists.

# Example:

# Input: [1, 2, 3], ['a', 'b', 'c']
# Output: [1, 'a', 2, 'b', 3, 'c']

def add_alternatives(lst1, lst2):
    final_lst = []
    for i in range(0,len(lst1)):
        final_lst.append(lst1[i])
        final_lst.append(lst2[i])
    return final_lst

print(add_alternatives([1, 2, 3], ['a', 'b', 'c']))