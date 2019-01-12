
def combinationSum2(candidates, target):
    setArr=set(candidates)
    returnArr=[]
    for i in range(0,len(candidates)):
        for j in range(i+1,len(candidates)):
            diff=target-candidates[i]-candidates[j]
            if diff in setArr:
                newArr=[candidates[i],candidates[j],diff]
                newArr.sort()
                if newArr not in returnArr:
                    returnArr.append(newArr)
    return returnArr

print(combinationSum2([2,3,5,7,4,1],7))


# def combinationSum2(candidates, target):
#     returnArr=[]
#     candidates.sort()
#     i=0
#     j=1
#     k=len(candidates)
#     while()
#         j=i+1
#         k=len(candidates)-1




    return returnArr
print(combinationSum2([2,3,5,7,4,1],7))