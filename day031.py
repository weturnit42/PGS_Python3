def solution(nums):
    answer = 0
    
    answer = len(list(set(nums)))
    
    if(answer > len(nums)/2):
        answer = len(nums)/2
    
    return answer