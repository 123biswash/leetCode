# Given a dictionary of words and a string made up of those words (no spaces),
#  return the original sentence in a list. If there is more than one possible
#  reconstruction, return any of them. If there is no possible reconstruction,
#  then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', 
# and the string "thequickbrownfox", you should return ['the', 'quick', 
# 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and 
# the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond]
#  or ['bedbath', 'and', 'beyond'].

def possibleReconstruction(givenSet, givenStr):
    returnArr=[]
    for i in range(0,len(givenStr)):
        for j in range(i+1,len(givenStr)):
            if givenStr[i:j+1] in givenSet:
                returnArr.append(givenStr[i:j+1])
                i=j
    return returnArr

givenSet=['quick','brown','the','fox']
givenStr='thequickbrownfox'
print('expected output: [ the, quick, brown, fox]')
print(possibleReconstruction(givenSet,givenStr))

givenSet1=['bed','bath','bedbath','and','beyond']
givenStr1='bedbathandbeyond'
print('expected output: [ bed, bath, and, beyond]')
print(possibleReconstruction(givenSet1,givenStr1))