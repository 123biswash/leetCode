
# [0,1,0,0]
# [0,0,1,0]
# [0,0,0,1]
# [1,0,0,1]

def uberPathBFS(arr, maxSteps, start):
    startRow=start[0]
    startCol=start[1]
    row=len(arr)
    col=len(arr[0])
    returnArr=[]
    for k in range(startRow-1, startRow+1, 1):
        for l in range(startCol-1, startCol+1, 1):
            if k>=0 and k<row and l>=0 and l<col and k!=startRow and l!=startCol:
                if k==startRow and l==startCol-1 and arr[k][l-1]==0:
                    returnArr.append([k,l-1])
                    arr[k][l-1]=2
                if k==startRow-1 and l==startCol and arr[k][l-1]==0:
                    returnArr.append([k-1,l])
                    arr[k-1][l]=2
                if (k==startRow+1 and l==startCol):
                    returnArr.append([k+1,l])
                    arr[k+1][l]=2
                if (k==startRow and l==startCol+1):
                    returnArr.append([k,l+1])
                    arr[k][l+1]=2
    return returnArr

arr=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,1]]
maxSteps=2
start=[2,1]
print(uberPathBFS(arr,maxSteps,start))