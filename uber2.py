# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

def findWord(string, board):
    board2=board
    #check for the first letter. if found check all neighboring cells within the index range
    # if found, recursively call the same function again on that neighbor and so on
    # if not found, keep going to the last cell, and if not found, return false
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if helper(i,j,0,string,board2):
                return True
    return False
            
def helper(boardIndexI, boardIndexJ, stringIndex, string, board):
    #take a string, take a given index, and see if the next index in the string belongs to 
    lenString=len(string)
    if stringIndex==len(string):
        return True
    row=len(board)
    col=len(board[0])
    
    # for i in range(boardIndexI-1, boardIndexI+1):
    if boardIndexI<0 or boardIndexI>row or board[boardIndexI][boardIndexJ]==0:
        return False
    else:
        if board[boardIndexI][boardIndexJ] == string[stringIndex]:
            board[boardIndexI][boardIndexJ]=0
            print("match !")
            print(boardIndexI)
            print(boardIndexJ)
            return helper(boardIndexI-1,boardIndexJ,stringIndex+1, string, board) or helper(boardIndexI+1,boardIndexJ,stringIndex+1, string, board) or helper(boardIndexI,boardIndexJ-1,stringIndex+1, string, board) or helper(boardIndexI,boardIndexJ+1,stringIndex+1, string, board)
    return False

string='SEE'
board =[['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
print(findWord(string, board))







