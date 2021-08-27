# 완전탐색 / 모의고사
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 정답이 순서대로 들은 배열=answers, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return (가장 높은 점수가 여러명이면 오름차순 정렬)
# ex) [1,3,2,4,2] > [1,2,3], [1,2,3,4,5] > [1]

import math
def solution(answers):
    people=[[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    corr=[0, 0, 0]
    answer=[]
    for p, peo in enumerate(people):            # 각 학생별  
        dou=math.ceil(len(answers)/len(peo))    # 문제의 개수가 people리스트 요소의 개수보다 많을 경우 반복
        peo=peo*dou
        for i in range(len(answers)):           # 정답 비교
            if peo[i]==answers[i]:
                corr[p]+=1                      # 각 학생별 정답 개수 
    cmax=max(corr)                              # 가장 많이 맞은 학생의 정답수

    for i in range(3):                          # 동점자가 있는 경우
        if corr[i]>=cmax:
            answer.append(i+1)
    return answer
