"""
Write a function to balance the parenthesis of a string.

The function will take as input a string of parenthesis (open and closed).
It will balance the parenthesis by removing the fewest possible characters
from the string, then return that shorter, balanced string.

A few examples:

balance("()")  -> "()"
balance(")(")  -> ""
balance(")()") -> "()"
balance("())") -> "()"
balance(")()") -> "()"
balance("(()") -> "()"
balance("(())") -> "(())"     !=  "()()"

(()(()(()))


"""

def balance(paren):
    openParenIndex=[]
    removeIndex=[]
    left=[]
    for i in range(len(paren)):
        if paren[i]=='(':
            left.append(paren[i])
            openParenIndex.append(i)
        else:
            if len(left)==0:
                removeIndex.append(i)
            else:
                left.pop()
                openParenIndex.pop()
    for k in openParenIndex[::-1]:
        temp1=paren[:k]+paren[k+1:]
        paren=temp1
    for j in removeIndex[::-1]:
        temp=paren[:j]+paren[j+1:]
        paren=temp
    return paren
print("(("+" Expected: ()") 
print("Output: ")  
print(balance("(("))
print(")()"+" Expected: ()") 
print("Output: ")  
print(balance(")()"))
print("())"+" Expected: ()") 
print("Output: ")  
print(balance("())"))
print(")()"+" Expected: ()") 
print("Output: ")  
print(balance(")()"))
print("(())"+" Expected: (())") 
print("Output: ")  
print(balance("(())"))
                 