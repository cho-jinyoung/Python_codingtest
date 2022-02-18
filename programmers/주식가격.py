# 프로그래머스 스택/큐  주식가격

# 효율성 0점, 정확도만 맞은 코드
'''def solution(prices):
    answer = []
    while prices:
        now=prices.pop(0)
        count=0
        for i, val in enumerate(prices):
            if now>val:
                count+=1
                break
            count+=1
        answer.append(count)
    return answer'''
  
# 리스트 요소를 pop할 때 deque를 쓰는 것 만으로도 효율성이 통과되었음
from collections import deque

def solution(prices):
    answer = []
    prices=deque(prices)
    while prices:
        now=prices.popleft()
        count=0
        for i, val in enumerate(prices):
            if now>val:
                count+=1
                break
            count+=1
        answer.append(count)
    return answer
  
  # 진짜 스택을 이용하여 풀음
  
