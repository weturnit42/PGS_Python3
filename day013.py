def solution(x, y, n): # y == 2^a * 3^b + n*c
    answer = 0

    pre = [x]
    post = []
    count = 0
    
    if(x == y):
        return 0
    
    while(True):
        post = []
        post = post+list(map(lambda x : x+n, pre))
        post = post+list(map(lambda x : x*2, pre))
        post = post+list(map(lambda x : x*3, pre))
        
        post = list(set(post))
        
        count = count+1
        
        tempMin = post[0]
        minimum = min([tempMin-n, tempMin/2, tempMin/3])
        if(minimum > y):
            count = -1
            break
        if(y in post):
            break
        pre = post
    answer = count
    return answer