def findkmin(arr, n):
  minNum=arr[0]
  x=0
  minIndex=0
  while(x<=n):
    for i in range(0,len(arr)-1):
      if(arr[i]<minNum):
          minIndex=i
          minNum=arr[i]
    temp=arr[minIndex]
    arr[minIndex]=arr[x]
    arr[x]=temp
    x+=1
  return arr[k]

arr1=[1,9,6,2,3,4,5]
k=3
print(findkmin(arr1, k))