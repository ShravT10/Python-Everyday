# Type: Logic Building
# Write a function char_frequency(s)
# that returns a dictionary with the frequency of each character (excluding spaces), ignoring case.

# Example:

# python
# Input: "Hello World"
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

def freq(s):
    dict = {}
    s = s.lower().replace(" ","")
    for i in s:
        dict[i] = dict.get(i,0) + 1
    
    return dict

print(freq("Hello world"))