import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while(len(scoville) > 1):
        a = heapq.heappop(scoville)
        
        if(a >= K):
            return answer
        b = heapq.heappop(scoville)
        
        heapq.heappush(scoville, a+b*2)
        
        answer = answer+1
        
    a = heapq.heappop(scoville)
    if(a<K):
        return -1
    else:
        return answer