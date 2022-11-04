# 스택/큐 -프린터 
# 인쇄 대기목록의 첫번째 문서보다 중요도가 높은 문서가 한 개라도 존재하면 대기목록의 가장 마지막으로 이동, 그렇지 않으면 인쇄
# 문서의 중요도 배열=priorities, 인쇄를 요청한 문서 위치=location이 주어질 때, 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return
# ex) [3, 3, 4, 2]=priorities, 3=location, return=4

# point idea: max값이 같지 않음, 맨 앞 문서를 출력하고 나면 max값이 달라짐


def solution(priorities, location):
    stack=[]
    pri=[[i,p]for i, p in enumerate(priorities)] # 현재 인덱스와 값 저장
    while len(priorities)!=0:               # 모두 출력할 때까지
        if priorities[0]<max(priorities):   # 대기 목록에서 중요도가 높은 문서가 있으면 
            pri.append(pri.pop(0))
            priorities.append(priorities[0])
        else :                              # 대기 목록에서 중요도가 높은 문서가 없으면
            stack.append(pri.pop(0))
        priorities.pop(0)    
    for i, p in enumerate(stack):           # 인쇄 순서
        if p[0]==location:                  # 처음 인덱스와 location값이 같은 경우
            return i+1                      # 인덱스+1 번째로 인쇄됨

        
        
# 비슷한데 deque를 이용한 풀이        
from collections import deque
def solution(priorities, location):
    answer = 0
    lists=deque()

    for i in range(len(priorities)):
        lists.append([i, priorities[i]])
    
    while lists:
        num, pri=lists.popleft()
        
        if len(lists)==0:
            answer+=1
            return answer
        
        for i in range(len(lists)):
            if pri < lists[i][1]:
                lists.append([num, pri])
                break
                
        if i==len(lists)-1:
            answer+=1
            if num==location:
                return answer
