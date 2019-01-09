from collections import deque
# squares = {x: x * x for x in range(10)}
# print(squares)

# dict={'a': 'adam', 'b':'bob', 'c':'cat'}

# print(dict.get('a'))

# lst=collections.deque(['A', 'B', 'C', 'D'])

# print(lst.index('A'))

def validParenthesis(str):
        if str=='':
            return True
        left=deque()
        star=deque()
        for i in range(len(str)){
                if str[i]=='*'):
                    star.append(str[i])
                elif str[i]='('):
                    left.append(str[i])
                else
                    if left.empty and star.empty():
                         return False
                    elif !left.empty:
                        left.pop()
                    else
                        star.pop()
        while !left.empty and !star.empty:
            left.pop
            star.pop
    return left.empty;

                 