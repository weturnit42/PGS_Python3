from collections import Counter
from itertools import combinations

def solution(clothes):
    answer = 0
    
    kind = []
    
    for cloth in clothes:
        kind.append(cloth[1])
    kindCount = Counter(kind)
    kindList = list(kindCount)
    # print(kindCount)
    # print(kindList)
    
    if(len(kindList) == 30):
        return 1073741823
    
    kindSetList = []
    for i in range(1, len(kindList)+1):
        kindSetList = kindSetList+list(combinations(kindList,i))
    
    for kindSet in kindSetList:
        temp = 1
        for kind in kindSet:
            temp = temp*kindCount[kind]
        answer = answer+temp
    return answer