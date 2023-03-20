def solution(weights):
    answer = 0
    
#     weights.sort()
    
#     for i in range(len(weights)):
#         for j in range(len(weights)):
#             if(i != j and weights[i] == weights[j]):
#                 answer = answer+1
#             if(weights[i] < weights[j]):
#                 continue
# #     10 10 10 20 20 -> 10 20 (10 두 개, 20 한 개)
#     weights = list(set(weights))
    
#     doubleWeights = list(map(lambda x : 2*x, weights))
#     tripleWeights = list(map(lambda x : 3*x, weights))
#     quadraWeights = list(map(lambda x : 4*x, weights))
    
#     weightList = doubleWeights+tripleWeights+quadraWeights
#     weightList.sort()

#     for i in range(len(weightList)):
#         for j in range(len(weightList)):
#             if(i != j and weightList[i] == weightList[j]):
#                 answer = answer+1
#             if(weightList[i] < weightList[j]):
#                 continue
#     answer = answer/2

    weightCount = [0]*901 #0번째 index가 100에 대응
    for i in range(len(weights)):
        weightCount[weights[i]-100] = weightCount[weights[i]-100]+1

    for i in range(len(weightCount)):
        for j in range(len(weightCount)):
            if((i+100)/2*3 == (j+100) or (i+100)/3*4 == (j+100) or (i+100)/2*4 == (j+100)):
                answer = answer+(weightCount[i]*weightCount[j])
                
    for i in range(len(weightCount)):
        if(weightCount[i] > 1):
            answer = answer+((weightCount[i])-1)*weightCount[i]/2
    
    return answer