def adhereRhymeScheme(poem, rhymeScheme):
    # dictionary to store repitions of a character in rhymeScheme
    wordDict={}
    # iterate through the rhymescheme to store the repitition index in the dictionary
    for i in range(0,len(rhymeScheme)):
        #if character not in dictionary, add key and add a value, which is the index it occurs in rhymeScheme 
        if rhymeScheme[i] not in wordDict:
            wordDict[rhymeScheme[i]] = [i]
        #if character is in dictionary, append the index to the list for that character
        else:
            wordDict[rhymeScheme[i]].append(i)
    #iterate through the dictionary to find characters that repeat 
    for word in wordDict:
        values=wordDict[word]
        #if only one repition found, then no need to check for whether it rhymes
        if len(values)==1:
            continue;
        #for words in the list, find the corresponding line in the poem and find the last index and compare with the next index int he list
        for j in range(0,len(values)-1):
            valA=poem[values[j]][-1]
            valB=poem[values[j+1]][-1]
            #call doWordsRhyme to check if the two words rhyme
            if not doWordsRhyme(valA,valB):
                #return false if they do not rhyme
                return False
    #if all cases pass, return True 
    return True


def doWordsRhyme(valA,valB):
  if valA=='cat' and valB=='pat':
    return True
  if valA=='rat' and valB=='bat':
    return True
  if valA=='mat' and valB=='lat':
    return True
  if valA=='dat' and valB=='pat':
    return True
  return False

print(adhereRhymeScheme([['love', 'is', 'rat'],['and', 'like', 'bat'],['love', 'is', 'lat'],['love', 'is', 'cat'],['love', 'is', 'pat']], 'AABBC'))