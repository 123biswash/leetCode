
def rotate(matrix):
    matrixArr=[[0 for x in range(len(matrix))] for x in range(len(matrix[0]))]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            matrixArr[i][j] = matrix[len(matrix)- 1 - j][i]
            
    return matrixArr

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

# 123
# 456
# 789

# 741
# 852
# 963
        
#         0,0 -> 2,0   
#         0,1 -> 1,0   
#         0,2 -> 0,0   
        
#         1,0 -> 2,1
#         1,1 -> 1,1
#         1,2 -> 0,1
        
#         2,0 -> 2,2
#         2,1 -> 1,2
#         2,2 -> 0,2