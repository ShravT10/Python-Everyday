# Write a function is_isogram(s) 
# returns True if the input string is an isogram, else False.

# Example:

# Input: "Machine"
# Output: True
# Input: "Programming"
# Output: False

def is_isogram(s): #machine
    a = []
    count = 0
    for i in s:
        a.append(i)
    for i in range(0,len(a)):
        for j in range(i+1,len(a)-1):
            if a[i]==a[j]:
                count+=1
    if count>1:
        return "is not an iso"
    else:
        return "is an iso"       
    
s = "machine"
b = "programming"
print(is_isogram(s))
print(is_isogram(b))

#simpler one

def iso(s):
    s = s.lower()
    return len(set(s)) == len(s)

print(iso(s))
    