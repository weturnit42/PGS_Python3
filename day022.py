import math

def solution(n):
    answer = 0
    
# #     1 1 2 3 5 8 13 21 34 ...
# #     피보나치 수열 일반항
# # 2 3+r5
# # 3 4+2r5
# # 4 7+3r5
# # 5 11+5r5
# # 6 18+8r5

# # r5/2의 홀수r제곱 (r5/2)^r == r5 * 5^((r-1)/2) * (1/2)^r
# # (-r5)/2의 홀수r제곱 (-r5/2)^r == r5 * 5^((r-1)/2) * (1/2)^r

# # ((1+r5)/2)^3 == (1/8) + (3r5/8) + (15/8) + (5r5/8)
#     fibo = []
    
#     for i in range(1, 1000+1):
#         posCoef = 0
#         for r in range(i+1):
#             if(r%2 == 1):
#                 # print(math.factorial(i) / math.factorial(r) / math.factorial(i-r), pow(5, (r-1)/2), pow(2, (-1)*r), math.factorial(i) / math.factorial(r) / math.factorial(i-r) * pow(5, (r-1)/2) * pow(2, (-1)*r))
#                 posCoef = posCoef+(math.factorial(i) // math.factorial(r) // math.factorial(i-r)) * pow(5, (r-1)/2) / pow(2, i) 
#         fibo.append(int(posCoef*2))
#     print(fibo[999])
# #     피사노 주기

    a = 1
    b = 1
    
    if(n==1):
        return a
    
    if(n==2):
        return b
    
    for i in range(n-2):
        temp = (a + b) % 1234567
        a = b % 1234567
        b = temp % 1234567
    
    answer = temp
    
    return answer
