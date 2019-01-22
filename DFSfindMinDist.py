# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# true is wall, false is not
# and start = (3, 0) (bottom left) 
# and end = (0, 0) (top left), 
# the minimum number of steps required
# to reach the end is 7, since we would
# need to go through (1, 2) because
# there is a wall everywhere else 
# on the second row.

def DFSfindMinDist(arr, start, end):
    startRow=start()[0]
    startCol=start()[1]
    endRow=end()[0]
    endCol=end()[1]
    row=len(arr)
    col=len(arr[0])
    size=1
    if startRow==endRow and startCol==endCol:
        return size
    else:
        if(startRow >= 0 and startCol < col):
            for i in range(startRow-1, startRow+1, 1):
                for j in range(startCol-1, startCol+1, 1):
                    if(arr[i][j]=='f'):
                        size+=
                        arr[i][j]='d'
                    newStart=(start()[0])
                    size+=DFSfindMinDist(arr, newStart, end)
        return size
    #size=0        
    #iterate from start row-1 to end row+1
        #iterate from start col-1 to end column+1
            #while row and col!=endRow and endCol
            #size+=1
            #if arr value at that index is false, size+=recursive func(arr, startBeingThatFunc)
            #if arr value is
            #
    return 0

def helper(arr, r, c):
    while(row)



arr1=[[f, f, f, f],[t, t, f, t],[f, f, f, f],[f, f, f, f]]
start1=(3,0)
end1=(0,0)
print(DFSfindMinDist(arr1, start1, end1))