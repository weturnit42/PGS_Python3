def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    pCount = 0
    yCount = 0
    
    for ch in s:
        if(ch == 'p' or ch == 'P'):
            pCount = pCount+1          
        if(ch == 'y' or ch == 'Y'):
            yCount = yCount+1
            
    return (pCount == yCount)