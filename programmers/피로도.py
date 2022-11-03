# 최소 필요 피로도 = 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
# 소모 피로도 = 던전을 탐험한 후 소모되는 피로도
# dungeons = [["최소 필요 피로도", "소모 피로도"], ... ] , 최소 필요 피로도 >= 소모 피로도
# k = 현재 피로도, return = 유저가 탐험할 수 있는 최대 던전 수


import itertools

def solution(k, dungeons):
    answer = 0
    dunge=list(itertools.permutations(dungeons, len(dungeons)))
    
    for dun in dunge:
        now=k
        count=0
        
        for i in dun:
            if i[0]<=now:
                count+=1
                now-=i[1]
            else:
                break
                
        answer=max(answer, count)
    return answer
