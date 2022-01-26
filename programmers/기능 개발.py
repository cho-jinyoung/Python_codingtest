# 스택/큐 - 기능개발
# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
# 순서대로 작업의 진도가 적힌 정수 배열=progresses, 각 작업의 개발 속도가 적힌 정수 배열=speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지 return
# ex) progress=[95, 90, 99, 99, 80, 90], speeds=[1, 1, 1, 1, 1, 1], return=[1, 3, 2]


# 통과하긴 했지만 너무 비효율적으로 우겨넣은 코드..그리고 문제의 의도인 스택/큐를 사용하지 않음
'''
import math
def solution(progresses, speeds):
    rest=[]
    answer=[]
    index=[]
    ans=[]
    count=0
    
    for i, pro in enumerate(progresses):
        rest.append(math.ceil((100-pro)/speeds[i]))   # ceil 함수를 안쓰기 위해 -((pro-100)//speeds[i])라고 쓸 수 있음
        
    max=rest[0]
    for i in range(1, len(rest)):
        if rest[i]>max:
            index.append(rest[i-1])
            answer.append(index)
            index=[]
            max=rest[i]
        else:
            index.append(rest[i-1])
            
    index.append(rest[-1])
    answer.append(index)   
    
    for i in range(len(answer)): # 
        ans.append(len(answer[i]))

    return ans
'''
  
# 스택/큐를 이용한 코드  
# 앞선 기능을 수행할 때 걸린 시간을 찾아 그 시간 내에 완성된 기능을 모두 pop하는 방식
def solution(progresses, speeds):
    time=0
    count=0
    answer=[]
    
    while len(progresses)>0:
        if (progresses[0]+speeds[0]*time)>=100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else :
            if count>0:
                answer.append(count)
                count=0
                time=0
            time+=1
    answer.append(count)
    return answer

# 나중에 한번 더 풀음! 스택은 안썼지만 시간 효율 굿
import math
def solution(progresses, speeds):
    answer=[]
    count, m=1, 0
    for i in range(len(progresses)):
        p=math.ceil((100-progresses[i])/speeds[i])  # 배포 가능 날짜
        if p>m: # 배포
            if m!=0: answer.append(count)           # 첫번째 경우 제외
            count=1
        else:   # 배포 가능 날짜가 앞 작업보다 빠른 경우
            count+=1   
        m=max(p, m) # 가장 빠른 배포 가능 날짜
    answer.append(count)    # 마지막 배포 가능 날 추가
    return answer
