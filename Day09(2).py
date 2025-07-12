# Write a function number_pyramid(n) 
# that prints a pattern like this:

# For n = 4:

# 1
# 1 2
# 1 2 3
# 1 2 3 4

def pyramid(n):
    pyr = ""
    for i in range(1,n+2):
        print(pyr)
        pyr = pyr + " " + str(i)

pyramid(4)