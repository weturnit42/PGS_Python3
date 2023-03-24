def solution(s):
    answer = True
    
    lcount = 0
    rcount = 0
    
    for ch in s:
        if(ch == "("):
            lcount = lcount+1
        if(ch == ")"):
            rcount = rcount+1
        
        if(lcount == rcount):
            lcount = 0
            rcount = 0
        
        if(rcount > lcount):
            return False
        
    if(lcount != rcount):
        return False
    
    return True