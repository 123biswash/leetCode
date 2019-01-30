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
    startRow=int(start[0])
    startCol=int(start[1])
    endRow=int(end[0])
    endCol=int(end[1])
    row=len(arr)
    col=len(arr[0])
    size=1
    if startRow==endRow and startCol==endCol:
        return size
    if arr[startRow][startCol]=='t':
        size=0
        return size
    else:
        if(startRow >= 0 and startCol < col and startRow<len(arr) and startCol>=0):
            for i in range(startRow-1, startRow+1, 1):
                for j in range(startCol-1, startCol+1, 1):
                    if(arr[i][j]=='f'):
                        if i!=startRow and j!=startCol:
                            newStart=[arr[i], arr[j]]
                            size+=DFSfindMinDist(arr, newStart, end)
                            arr[i][j]='d'        
    # if arr[]
    return size
arr1=[['f', 'f', 'f', 'f'],['t', 't', 'f', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']]
start1=[3,0]
end1=[0,0]
print(DFSfindMinDist(arr1, start1, end1))