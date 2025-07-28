# # Write a function rotate_matrix(matrix) 
# # that rotates a square matrix 90° clockwise.

# Input:
# [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

# Output:
# [
#  [7, 4, 1],[0][0] -> [0][2]
#  [8, 5, 2],[1][0] -> [0][1]
#  [9, 6, 3] [2][0] -> [0][0]
# ]

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

rotated = rotate_matrix(matrix)

for row in rotated:
    print(row)
