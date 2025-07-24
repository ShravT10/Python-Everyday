# #Write a function transpose(matrix) that returns the transpose of a 2D list.
# 📌 A transpose flips rows into columns.

# Input: [[1, 2, 3],
#         [4, 5, 6]]

# Output: [[1, 4],
#          [2, 5],
#          [3, 6]]

def tranpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
print(tranpose([[1, 2, 3],[4, 5, 6]]))