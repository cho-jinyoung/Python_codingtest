# beakjoon 6588 골드 바흐의 추측

# 소수 판별시 에라토스테네스의 체 이용 > 여러 수의 소수 판별시 용이
# 1. 2는 소수 > 나머지 수 중 2의 배수 모두 지움
# 2. 다음 작은 소수 3 > 나머지 수 중 3의 배수 모두 지움
# 3. 반복

# 에라토스네스의 체의 특성을 이용해 주어진 조건 범위 내 소수를 먼저 모두 찾고 시작
import sys

alllist=[False, False]+[True]*1000000 # 0,1 제외
    
for k in range(2, 1000001):
    if alllist[k]:
        for i in range(k+k, 1000001, k):   # 소수의 배수 지움
            alllist[i]=False

while True:
    ni=int(sys.stdin.readline())    # input보다 시간 단축
    if ni==0:
        break
    
    i=0
    #flag=1
    for i in range(2, 1000001):
        if alllist[ni-i] and alllist[i] and (ni-1)>0:
            print(ni, '=', i,'+', ni-i)    
            break
        i+=1
    else:       # for-else문 > for문이 다 돌면 들어옴
        print("Goldbach's conjecture is wrong.")        
      
