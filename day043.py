from itertools import permutations

def solution(numbers):
    answer = 0
    stringCandidates = []
    candidates = []
    numbers = list(numbers)
    
    for i in range(1, len(numbers)+1):
        for _ in list(permutations(numbers, i)):
            stringCandidates.append(_)
    
    for i in range(len(stringCandidates)):
        temp = ''
        
        for j in range(len(stringCandidates[i])):
            temp = temp+stringCandidates[i][j]
        
        candidates.append(int(temp))
    
    for i in range(candidates.count(0)):
        candidates.remove(0)
    for i in range(candidates.count(1)):
        candidates.remove(1)
    candidates = list(set(candidates))
    
    for candidate in candidates:
        test = 2
        
        primeCheck = True
        while(test <= pow(candidate, 0.5)):
            if(candidate % test == 0):
                primeCheck = False
                break
            test = test+1
            
        if(primeCheck == True):
            answer = answer+1
            
            
    return answer