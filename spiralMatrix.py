def spiralPrint(row,col,arr):
    nRow=0
    nCol=0
    while (nRow<row and nCol<col):
        #print first row from remaining rows
        for i in range(nCol,col):
            print(arr[nRow][i])
        nRow+=1
        #print last column from remaining columns
        for j in range(nRow, row):
            print(arr[j][col-1])
        col-=1
        if nRow<row:
            #print last row from remianing rows
            for k in range(col-1,nCol-1,-1):
                print(arr[row-1][k-1])
            row -=1
        if nCol<col:
            # print first column from remaining columns
            for l in range(row-1, nRow-1,-1):
                print(arr[l][nCol])
            nCol +=1
    return
arr = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 
        
R = 3; C = 6
spiralPrint(R, C, arr) 