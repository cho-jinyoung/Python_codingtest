# 그냥 구현, 아래의 코드는 정확성은 모두 맞지만 효율성부분에서 점수를 받을 수 없음
def solution(food_times, k):
    l=len(food_times)
    s, i=0, 0

    while True:
        if food_times[i%l]>0:      # 음석 먹기
            food_times[i%l]-=1
            s+=1
            count=0
        else:   count+=1           # 다 먹은 음식인 경우
            
        if count>=l:    return -1  # 음식을 전부 다 먹은 경우
        if s==(k+1):    break      # 네트워크가 멈춘 상태            
        i+=1                       # 현재 음식 인덱스
    return (i%l+1)
  
###################################################################

# 우선순위 큐를 이용해 접근, 가장 적은 시간이 걸리는 음식부터 먹음
import heapq

def solution(food_times, k):
    hq=[]
    now, pre, alltime=0, 0, 0
    # now=현재 음식 먹는데 걸리는 시간, pre=이전 음식을 먹는데 걸린 시간(그 시간동안 다 먹은 음식 체크)
    l=len(food_times)
    
    if sum(food_times)<=k:
        return -1
    
    for i, val in enumerate(food_times):
        heapq.heappush(hq, (val, i+1))
        
    while alltime+((hq[0][0]-pre)*l)<=k:
        if k<(now+alltime):
            break
        now=heapq.heappop(hq)[0]
        
        alltime+=(now-pre)*l      # 음식을 먹는데 걸리는 시간
        l-=1            # 다 먹었으니 음식 개수 -1
        pre=now
    r=sorted(hq, key=lambda x:x[1])    # 남은 음식의 인덱스 순으로 정렬
    return r[(k-alltime)%l][1]
