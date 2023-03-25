def solution(progresses, speeds):
    answer = []
    
    while len(progresses) != 0:
        queue = []
        
        for i in range(len(progresses)):
            progresses[i] = progresses[i]+speeds[i]
            
        i = 0  
        while True:
            if(i == len(progresses)):
                break
            
            if(progresses[i] < 100):
                i=i+1
                break
            if(progresses[i] >= 100):
                queue.append(progresses[i])
                del speeds[i]
                del progresses[i]
                
        if(len(queue) != 0):
            answer.append(len(queue))
        
    return answer