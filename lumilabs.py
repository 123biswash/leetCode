def returnTriplets(input):
    maxVal=input[0][0]
    for i in input:
        if i[0] > maxVal:
            maxVal=i[0]
    storeDict={}
    tripletDict={}
    superTripletArr={}
     #storing all websites visited by user in a dictionary where key is user number and value is array of websites in respective order
    for j in range(len(input)):
        storeDict[input[j][0]].append(input[j][1])
    for k in range(len(storeDict)):
        tempArr=storeDict[k]
        for l in range(len(tempArr)):
            triplet=tempArr[i:i+3]
            tripeletDict[k].append(triplet)
    for m in range(len(tripletDict)):
        #for each key in triplet dict, traverse through the values and 
        #
    
    # 1: [A, B, C],[B, C, D], [C,D,E]
    # 2: [B, C, D],[C,D,E]
    # 3: A


# 
# Your previous Plain Text content is preserved below:
# 
# Given a log file with each row representing <user_id> <page_url>, write a method to return 10 most common triplets. A triplet is defined as a collection of 3 pages visited in a consecutive sequence by a user. So if there are 5 pages: A, B,C, D, E and following log file:
# 
# 1 A
# 1 B
# 2 B
# 3 A
# 2 C
# 1 C
# 1 D
# 1 E
# 2 D
# 2 A
# 2 E
# 
# Then the most common triplet is: BCD since it’s visited by both 1 and 2.
# 
# #max number of users. make that many arrays to store each user's website visits consecutively
# 

