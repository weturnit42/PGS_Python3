def solution(cards1, cards2, goal):
#     answer = 'Yes'
#     wordIndex1 = []
#     wordIndex2 = []
    
#     for word in goal:
#         try:
#             wordIndex1.append(cards1.index(word))
#         except ValueError:
#             continue
#         try:    
#             wordIndex2.append(cards2.index(word)) 
#         except ValueError:
#             continue
            
#     if(sorted(wordIndex1) != wordIndex1):
#         answer = 'No'
#     if(sorted(wordIndex2) != wordIndex2):
#         answer = 'No'
    
    answer = 'Yes'
    wordList = []
    
    i=0
    j=0
    k=0
    
    for word in goal:
        if(i<len(cards1) and word == cards1[i]):
            i=i+1
            k=k+1
            wordList.append(word)
        elif(j<len(cards2) and word == cards2[j]):
            j=j+1
            k=k+1
            wordList.append(word)
        else:
            answer = 'No'
            break
        
        # if(k == len(goal)-1 and wordList != goal):
        #     answer = 'No'
        #     break
        # elif(k == len(goal)-1 and wordList == goal):
        #     answer = 'Yes'
        #     break
        # if(k == len(goal)-1):
        #     break
    
    return answer