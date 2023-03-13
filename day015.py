def solution(s):
    answer = [-1]*len(s)
    
    '''
    b      b
    ba     ab
    ban    nab
    bana   anab
    banan  nanab
    banana ananab
    
    a    a
    aa   aa
    aab  baa
    aabb bbaa
    '''
    
    for i in range(1, len(s)):
        if(s[i] in s[0:i]):
            answer[i] = (list(reversed(list(s[0:i]))).index(s[i]))+1
    return answer