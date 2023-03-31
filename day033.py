from collections import Counter

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        # for j in range(i+1, len(phone_book)):
        #     if(phone_book[j].find(phone_book[i]) == 0):
        #         answer = False
        #         break
        # if(answer == False):
        #     break
        if(phone_book[i+1].find(phone_book[i]) == 0):
            answer = False
            break

#     lenList = []
#     for i in range(len(phone_book)):
#         lenList.append(len(phone_book[i]))
#     minLen = min(lenList)
    
#     prefix = []
#     for i in range(len(phone_book)):
#         for j in range(len(prefix)):
#             # print(prefix[j], phone_book[i])
#             if(phone_book[i].find(prefix[j]) == 0):
#                 return False
#         for j in range(len(phone_book[i])):
#             prefix.append(phone_book[i][:j+1])
            
    # prefix = [[] for i in range(len(phone_book))]
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book[i])):
#             prefix[i].append(phone_book[i][:j+1])
            
#     for i in range(len(phone_book)):
#         for j in range(len(prefix)):
#             for k in range(len(prefix[j])):
#                 # print(phone_book[i], prefix[j][k])
#                 if(i != j and prefix[j][k].find(phone_book[i]) == 0):
#                     return False

#     lenList = []
#     for i in range(len(phone_book)):
#         lenList.append(len(phone_book[i]))
#     minLen = min(lenList)
#     # print("minLen", minLen)
    
#     phone_book.sort()
    
#     prefix = {}
#     for i in range(len(phone_book)):
#         # print(minLen, len(phone_book[i])+1
#         for j in range(minLen, len(phone_book[i])+1):
#             # print(phone_book[i][:j], phone_book[i])
#             # if(phone_book[i][:j] in prefix and len(phone_book[i]) <= len(phone_book[i][:j])):
#             #     return False
#             # if(phone_book[i][:j] in prefix):
#             #     continue
#             prefix[phone_book[i][:j]] = phone_book[i]
#     for i in range(len(phone_book)):
#         for key in prefix:
#             # print(phone_book[i], key, prefix[key])
#             if(phone_book[i].find(key) == 0 and phone_book[i] != key):
#                 return False
    
#     lenList = []
#     for i in range(len(phone_book)):
#         lenList.append(len(phone_book[i]))
#     minLen = min(lenList)
    
#     prefix = []
#     for i in range(len(phone_book)):
#         for j in range(minLen, len(phone_book[i])+1):
#             prefix.append(phone_book[i][:j])
            
#     prefixCount = Counter(prefix)
#     # print(prefixCount)
#     for cnt in prefixCount:
#         if(prefixCount[cnt] >= 2):
#             return False

    
        
    return answer