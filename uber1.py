# func decode(code string) []string {}
# (in no particular order, in coding language of choice)
# decode("122") => ["abb", "av", "lb"]
# decode("122615") => ["abbfae" "abbfo" "abzae" "abzo" "avfae" "avfo" "lbfae" "lbfo" "lzae" "lzo"]

#for each char in the num string, 
#122615
#^
# 1 22615
# 12 2615

def decode(string):
    tempString=''
    returnList=[]
    letterList=[]
    for i in range(len(string)):
        returnList.append(helper(string[i:]))
    for i in range(len(string)):
        tempString+=string[i]
    returnList.append(tempString)
    return returnList
        
def helper(string):
    returnArr=[]
    if string=='':
        return
    if len(string)==2:
        firstVal=string[0]
        secondVal=string[1]
        combinedVal=string[0:1]
        #check for if combiledVal is in the charMap
        returnArr.append(charMap[firstVal])
        returnArr.append(charMap[secondVal])
        if combinedVal in charMap:
          returnArr.append(charMap[combinedVal])
        return returnArr
    firstArr=helper(string[1:])
    for i in range(len(firstArr)):
        returnArr.append(string[0] + firstArr[i])
    
    return returnArr
    #122615
    #1 22615
    #12 2615
    
    # 2615
    # 2 615
    
    # 26 15
    # 6 1 5 
    
    # 15
    # 1 5
    # 15 ''

charMap = {
	"1":  "a",
	"2":  "b",
	"3":  "c",
	"4":  "d",
	"5":  "e",
	"6":  "f",
	"7":  "g",
	"8":  "h",
	"9":  "i",
	"10": "j",
	"11": "k",
	"12": "l",
	"13": "m",
	"14": "n",
	"15": "o",
	"16": "p",
	"17": "q",
	"18": "r",
	"19": "s",
	"20": "t",
	"21": "u",
	"22": "v",
	"23": "w",
	"24": "x",
	"25": "y",
	"26": "z",
}

num='122'
print(decode(num))
