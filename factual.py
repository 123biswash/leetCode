
def solution(inputTable):
    # Type your solution here 
    returnDict={}
    maxNum=0
    maxName=''
    for j in inputTable:
        if j[0] in returnDict:
                returnDict[j[0]].append(j)
                sortedDict=sorted(returnDict[j[0]], key = lambda x: str(x[1]))
                returnDict[j[0]]=sortedDict
        else:
            returnDict[j[0]]=[j]    
    for j in returnDict:
        arrSize = len(returnDict.get(j[0])
        # print(returnDict.get(j[0])
        if arrSize > maxNum:
            maxNum=arrSize
            maxName=j[0]  
    returnArr=[[]]
    i=0
    for key in returnDict:
        for l in range(0,max):
            if returnDict.get(maxName)[l][1]==returnDict.get(key)[l][1]:
                returnArr[i][l]=returnDict.get(key)[l][2]
            else:
                returnArr[i][l]=null
            i=i+1
    return returnArr

inputTable=[['Boston', 'Mexican','120'],['Boston','American','100'],['Los Angeles','Mexican','400'],['Los Angeles','American', '200'],['Los Angeles', 'Smoothies', '100']]
solution(inputTable)