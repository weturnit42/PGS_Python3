def solution(sizes):
    answer = 0
    
    for size in sizes:
        size.sort()
    
    wMax = 0
    hMax = 0
    
    for size in sizes:
        if(size[0] > wMax):
            wMax = size[0]
        if(size[1] > hMax):
            hMax = size[1]
            
    answer = wMax * hMax
    return answer