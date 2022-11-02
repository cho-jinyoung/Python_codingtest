# 스택/큐
# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거한 수를 return (순서 유지)
# ex) arr = [1, 1, 3, 3, 0, 1, 1], return = [1, 3, 0, 1] / arr = [4, 4, 4, 3, 3], return = [4, 3]


from collections import deque
def solution(arr):
    answer=[]
    arr=deque(arr)
    answer.append(arr.popleft())
    
    for _ in range(len(arr)):
        a=arr.popleft()
        
        if answer[-1]!=a:
            answer.append(a)
            
    return answer
