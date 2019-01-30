# for row in range(0,len(matrix)):
#     for column in range(0,len(matrix[0])):
#         if (matrix[row][column]==2):
#             matrix[row][column]=1
# for row in range(0,len(matrix)):
#     for column in range(0,len(matrix[0])):
#         print matrix[row][column],
# return maxRegion

def getRegionSize(matrix,r,c):
    row=len(matrix)
    col=len(matrix[0])
    if (r<0 or r > row-1 or c<0 or c>col-1):
        size = 0
        return size
    if matrix[r][c]!=1:
        size = 0
        return size
    matrix[r][c]=2
    size=1
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if i!=r or j!= c:
                size+=getRegionSize(matrix,i,j)
    return size

# [0,0,0,1,1,0,0]
# [0,1,0,0,1,1,0]
# [1,1,0,1,0,0,1]
# [0,0,0,0,0,1,0]
# [1,1,0,0,0,0,0]
# [0,0,0,1,0,0,0]
def getBiggestRegion(matrix):
    maxRegion=0
    for row in range(0,len(matrix)):
        for column in range(0,len(matrix[0])):
            if(matrix[row][column]==1):
                size=getRegionSize(matrix,row,column)
                maxRegion=max(size,maxRegion)
    return maxRegion
matrix = [[0,0,0,1,1,0,0],[0,1,0,0,1,1,0],[1,1,0,1,0,0,1],[0,0,0,0,0,1,0],[1,1,0,0,0,0,0],[0,0,0,1,0,0,0]]
print(getBiggestRegion(matrix))
