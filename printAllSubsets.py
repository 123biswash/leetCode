#[a,b,c,d,e]

def printAllSubsets(arr):
    returnArr=[[]]
    # returnArr.append([''])
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)+1):
            returnArr.extend([arr[i:j]])
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)-1):
            tempArr=[]
            temp=''
            temp=(arr[i])
            k=j+1
            while(k<=len(arr)-1):
                temp+='\','+(arr[k])
                k=k+1
            returnArr.append([temp])
            tempArr=[]
    return returnArr


print(printAllSubsets(['a','b','c']))
