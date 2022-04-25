# beakjoon 14501
# DP 현재 시점에서 최선인 것 

import sys

input=sys.stdin.readline

n=int(input())
lists=[]    # 입력 값
dp=[0]*(n+1)       # x일에 받을 수 있는 최대 금액

for i in range(n):
    lists.append(list(map(int, input().split())))
    
for i in range(1, n+1):  # i일에 돈을 얼마 벌었는지
    # i일 미만의 일자를 거치면서 1) i일에 일이 끝난 경우, 2) i일 이전에 이미 끝난 경우를 나눠 올라옴
    for j in range(0, i):   
        # 2) j번째 날에 일을 안하고(진행중인 일이 없음) i일까지 온 경우
        dp[i]=max(dp[i],dp[j])  # i일 이전에 일이 끝났는데 현재 번 것보다 많으면 갱신
        
        # 1) j번째 날에 일을 한 경우
        if (lists[j][0]+j==i):  # 현재(i)일에 일이 끝난 경우 = 돈을 받음
            dp[i]=max(dp[i],dp[j]+lists[j][1])
print(max(dp))
