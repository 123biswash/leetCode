# 123   # 741
# 456   # 852
# 789   # 963
#         0,0 -> 2,0            0,1 -> 1,0          0,2 -> 0,0
#         1,0 -> 2,1            1,1 -> 1,1          1,2 -> 0,1
#         2,0 -> 2,2            2,1 -> 1,2          2,2 -> 0,2

# For in-place
    # 1) Move elements of top row.
    # 2) Move elements of last column.
    # 3) Move elements of bottom row.
    # 4) Move elements of first column.
# #IN-PLACE
# def rotateInPlace(matrixIn):
#     h=len(matrixIn)
#     w=len(matrixIn[0])

#     for i in range(0,w):
#         matrixIn[0][i] = matrixIn[h-1-i][0]

#     for j in range(1,h):
#         matrixIn[j][w-1] = matrixIn[0][j]

#     for k in range(0,w-1):
#         matrixIn[h-1][k]=matrixIn[h-1-k][w-1]

#     for l in range(1,h-1):
#         matrixIn[l][0]=matrixIn[h-1][l]

#     return matrixIn

# # NOT IN-PLACE
# def rotate(matrix):
#     matrixArr=[[0 for x in range(len(matrix))] for x in range(len(matrix[0]))]
#     for i in range(0,len(matrix)):
#         for j in range(0,len(matrix)):
#             matrixArr[i][j] = matrix[len(matrix)- 1 - j][i]   
#     return matrixArr



def rotate(matrixIn):
    matrixArr=[[0 for x in range(len(matrixIn))] for x in range(len(matrixIn[0]))]
    h=len(matrixIn)
    w=len(matrixIn[0])

    for i in range(0,w):
        matrixArr[0][i] = matrixIn[h-1-i][0]

    for j in range(1,h):
        matrixArr[j][w-1] = matrixIn[0][j]

    for k in range(0,w-1):
        matrixArr[h-1][k]=matrixIn[h-1-k][w-1]

    for l in range(1,h-1):
        matrixArr[l][0]=matrixIn[h-1][l]
   
    return matrixArr

input=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
for i in input:
    print(i)
print("/n")

result=rotate(input)
for i in result:
    print(i)