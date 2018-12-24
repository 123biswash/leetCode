import math
class Solution(object):
    def removeKdigits(self, num, k):
        #1432219, k=3
        
        if (len(num)==k): 
            return '0'
        lenLeft=len(num)-k
        newStr=''
        minIndex=0
        while((minIndex<len(num)-1) and lenLeft>0):
            for l in range (minIndex,len(num)-1):
                minVal=num[minIndex]
                intNum=int(num[l])
                intMinVal=int(minVal)
                if(intNum < intMinVal):
                    if(len(num)-l>=k):
                        minVal=num[l]
                        minIndex=l
            newStr+=minVal
            minIndex=minIndex+1
            lenLeft-=1
            print("Test")
        return newStr

def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            num = stringToString(line)
            line = lines.next()
            k = stringToInt(line)
            
            ret = Solution().removeKdigits(num, k)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()\