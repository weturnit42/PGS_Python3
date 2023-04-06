import heapq

def solution(operations):
    answer = []
    
    doublePriorityQueue = []
    heapq.heapify(doublePriorityQueue)
    
    for i in range(len(operations)):
        if(operations[i].split()[0] == 'I'):
            # print(operations[i].split()[0], operations[i].split()[1])
            heapq.heappush(doublePriorityQueue, int(operations[i].split()[1]))
            
        elif(operations[i] == "D 1"):
            maxHeap = []
            heapq.heapify(maxHeap)
            for item in doublePriorityQueue:
                heapq.heappush(maxHeap, -item)
            maxVal = heapq.heappop(maxHeap)
            doublePriorityQueue.remove(-maxVal)
            heapq.heapify(doublePriorityQueue)
        elif(operations[i] == "D -1"):
            heapq.heappop(doublePriorityQueue)
            
    if(len(doublePriorityQueue) == 0):
        return [0, 0]
    
    minVal = doublePriorityQueue[0]
    for item in doublePriorityQueue:
         heapq.heappush(doublePriorityQueue, -item)
    maxVal = doublePriorityQueue[0]
    return [minVal, maxVal]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))