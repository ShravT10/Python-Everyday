# Write a function unique_union(list1, list2) 
# that returns a list of unique elements present in either of the two lists (union, no duplicates).

# Example:

# python
# Copy
# Edit
# Input: [1, 2, 3], [3, 4, 5]
# Output: [1, 2, 3, 4, 5]

def unique(lst1,lst2):
    lst = lst1 + lst2
    ret = []
    for i in lst:
        if i not in ret:
            ret.append(i)

    return sorted(ret)

print(unique([1, 2, 3 , 6 , 5,7,8,8,3,2,1], [3, 4, 5]))
    

def unique_union(list1, list2):
    return list(set(list1) | set(list2))

# Test
print(unique_union([1, 2, 3], [3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
