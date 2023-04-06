import heapq

def solution(jobs):
    answer = 0
    tick = 0
    
    turnaroundTime = []
    
    heapq.heapify(jobs)
    
    while(len(jobs) != 0):
        proc = [0, 10000]
        for job in jobs:
            if(job[0] <= tick and job[1] < proc[1]):
                proc = job
            
        if proc == [0, 10000]:
            process = heapq.heappop(jobs)
            tick = process[0]
            
            tick = tick+process[1]
            turnaroundTime.append(tick - process[0])
        else:
            process = proc
            jobs.remove(proc)
            heapq.heapify(jobs)
            
            tick = tick+process[1]
            turnaroundTime.append(tick - process[0])
        
    answer = sum(turnaroundTime) // len(turnaroundTime)
    return answer