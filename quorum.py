#given a string remove a set of characters with the following charateristics: the characters are same but one is uppercase and another is lowercase
# eg: 
# input: abBc, output: ac
# input: hgjdDchJjq, output: hgjchq
# input: reddit, output: reddit
#in ASCII, lower and uppercase letter for same letter is 32 apart

def removeAdjacentUpperLower(givenString):
    for i in range(0,len(givenString)-1):
        if abs(ord(givenString[i])-32==ord(givenString[i+1])):
            newString=givenString[:i-1]+givenString[i+2:]
            print(newString)
            return removeAdjacentUpperLower(newString)
    return givenString

print("input: " + "hgjdDchJjq")
print("expected output: " + "hgjchq")
print("output:" + removeAdjacentUpperLower('hgjdDchJjq'))