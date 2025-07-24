# #Write a function generate_pascals_triangle(n) 
# # that returns a list of lists representing Pascal's Triangle with n rows.

# Input: n = 5
# Output:
# [
#  [1],
#  [1, 1],
#  [1, 2, 1],
#  [1, 3, 3, 1],
#  [1, 4, 6, 4, 1]
# ]

def generate_pascals_triangle(n):
    finallst = [[1],[1,1],[1,2,1]]
    while len(finallst) != n:
        ref = finallst[-1]
        new_lst = []
        for num in range(1,len(ref)):
            new_lst.append(ref[num-1]+ref[num])
        new_lst = [1] + new_lst + [1]
        finallst.append(new_lst)
    
    return finallst
    

for row in generate_pascals_triangle(10):
    print(row)
