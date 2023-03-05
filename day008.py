def solution(wallpaper):
    answer = []
    xCor = []
    yCor = []
    lux = 0
    luy = 0
    rdx = 0
    rdy = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j] == '#'):
                yCor.append(j)
                xCor.append(i)
                
    lux = min(xCor)
    luy = min(yCor)
    rdx = max(xCor) + 1
    rdy = max(yCor) + 1
    
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
    
    return answer