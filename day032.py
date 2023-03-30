from collections import Counter

def solution(participant, completion):
    answer = ''
    
    pCount = Counter(participant)
    cCount = Counter(completion)
    
    participant = list(set(participant))
    
    for name in participant:
        # print(pCount[name], cCount[name])
        if(pCount[name] != cCount[name]):
            return name
    return answer