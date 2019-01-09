

def sumWithoutI(arr):
    print(len(arr))
    resultArr=[1] * len(arr)
    for i in range(0,len(arr)): 
        for j in range(0, len(arr)) :
            if (j!=i):
                resultArr[i]=resultArr[i] * arr[j]
    return resultArr

def recursiveMultiply(arr):
    returnProduct=1
    for i in arr:
        returnProduct*=i
    return 
arr=[1,2,3,4,5]
print(sumWithoutI(arr))