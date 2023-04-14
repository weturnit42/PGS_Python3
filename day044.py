def solution(brown, yellow):
    answer = []
    
    div = 1
    while(div <= pow(yellow, 0.5)):
        if(yellow%div == 0):
            if((div+2)*(yellow//div+2) == brown+yellow):
                return [yellow//div+2, div+2]
        
        div = div+1
        
    return answer