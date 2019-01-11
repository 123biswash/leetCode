# parse_query_params('https://google.com?a=1&b=2') # { 'a': '1', 'b': '2' }
# parse_query_params('https://google.com?a=1&b=2&cat=hello') # { 'a': '1', 'b': '2', 'cat': 'hello' }

#returnArr=[]
#find ? and set rest of the string to new string
#split string with & and put into a list that would look like ['a=1','b=2'...]
#for each element in that list, append the first index's value to key and last to the value int the dictionary

def parse_query(sent):
    returnDict={}
    questionIndex=sent.find('?') 
    restOfString=sent[questionIndex+1:] 
    fullList=restOfString.split('&')
    for i in fullList:
        tempArr=i.split('=')
        returnDict[tempArr[0]] = tempArr[1]
    return returnDict
    
    
def two_sum(target, numArr):
    returnArr=[]
    #store in a set with O(1) lookup time
    setArr=set(numArr)
    #put each element of numArr in a dictionary
    for j in range(0,len(numArr)):
        anotherElement=target-numArr[j]
        if anotherElement in setArr:
            k=numArr.index(anotherElement)
            tempArr=[min(j,k), max(j,k)]
            if tempArr not in returnArr:
                returnArr.append(tempArr)
    return returnArr

print(two_sum(10, [1, 3, 2, 5]))
# (1, 2)
#for each element, if there exists another element such that target-element=anotherElement, then return the index of element and another element as tuple

    


