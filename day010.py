def solution(s, skip, index):
    answer = ''
    
    for ch in s:
        temp = ord(ch)
        i = 0
        while(i<index):
            temp = temp+1
            if(temp > ord('z')):
                temp = temp-26
            if(chr(temp) in skip):
                continue
            else:
                i=i+1
        answer = answer+chr(temp)
                
    return answer