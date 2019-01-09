# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

def autoComplete(word, arr):
    returnArr=[]
    for i in range(0,len(arr)):
        temp = arr[i]
        if temp[0:len(word)]==word:
            returnArr.append(arr[i])
    return returnArr

arr = ['dog', 'deer', 'deal']
word='de'

print(autoComplete(word, arr))