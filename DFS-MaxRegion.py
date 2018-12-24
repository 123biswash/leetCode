def getBiggestRegion(matrix):
    maxRegion=0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            # if (matrix [row][column] == 1):
            #     size=getRegionSize(matr)
            print(matrix[row][column])



matrix = [[0,0,0,1,1,0,0],[0,1,0,0,1,1,0],[1,1,0,1,0,0,1],[0,0,0,0,0,1,0],[1,1,0,0,0,0,0],[0,0,0,1,0,0,0]]
getBiggestRegion(matrix)
