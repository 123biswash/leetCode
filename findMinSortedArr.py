def findMinSortedArr(arr):
    low=0
    lenArr=len(arr)
    mid = (lenArr-low/2)-1
    minVal=0
    if arr[mid]<arr[lenArr-1]:
        return
    if arr[low]<arr[mid]:
        return
    return minVal

arr = [5, 6, 1, 2, 3, 4] 
n=len(arr)
print("The minimum element is: " + str(findMinSortedArr(arr1,0,n-1)))