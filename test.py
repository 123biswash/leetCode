from collections import deque

def validParenthesis(str):
    if str=='':
        return True
    left=deque()
    star=deque()
    for i in range(len(str)):
        if str[i]=='*':
            star.append(str[i])
        elif str[i]=='(':
            left.append(str[i])
        else:
            if not left and not star:
                return False
            elif left:
                left.pop()
            else:
                star.pop()
    while left and star:
        if left.top > star.top: 
            return False
        left.pop()
        star.pop()
    return left.empty;

print(validParenthesis('{{{}}}**'))