class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if (len(num)==k):
            return '0'

        lenLeft=len(num)-k
        newStr=''
        minIndex=0
        minVal=num[0]

        while(lenLeft > 0):
            minVal=num[minIndex+1]
            for l in range (minIndex+2,len(num)):
                afterbound=len(num)-l
                if((num[l] < minVal) && (afterbound > lenLeft)):
                    minVal=num[l]
                    minIndex=l

                if((afterbound<lenLeft)&&

            newStr+=minVal
            lenLeft-=1

        return newStr
        

        # /*
        # if(len(num)-l==k):
        #             for m in range(l+1,len(num)-1):
        #                 if(lenLeft>0):
        #                     afterStr+=num[m]
        #             print("the string is" + afterStr)
        #             lenLeft=0
        #             break
        # */