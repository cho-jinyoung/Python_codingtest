# beakjoon 14501
# DFS 가능한 경우의 수의 최대값 갱신

import sys

input=sys.stdin.readline

n=int(input())
lists=[]    # 입력 값
dp=[0]*(n+1)       # x일에 받을 수 있는 최대 금액
global ans
ans=0

for i in range(n):
    lists.append(list(map(int, input().split())))
    
def dfs(start, sum):
    global ans
    if start>n:
        return
    ans=max(ans, sum)
    for i in range(start, n):
        dfs(i+lists[i][0], sum+lists[i][1])
dfs(0,0)        
print(ans)
