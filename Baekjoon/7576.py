# beakjoon 7576 토마토
# BFS > 1(익은 토마토)를 기준으로 하루가 지날 때마다 옆에 있는 토마토 익히기, 더 이상 익을 수 있는 토마토가 없을 때까지
# 며칠 걸리는지 세어야 하므로 DFS가 아닌 BFS
# deque를 안쓰면 시간초과

from collections import deque
import sys
#sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m=map(int, input().split())   # (m,n)
q=[]

tomato=[[0]*n]*m
for i in range(m):      # 입력과 동시에 익은 토마토 체크
    tomato[i]=list(map(int, input().split()))
    for j in range(n):
        if tomato[i][j]==1:
            q.append([i, j])            
def bfs():
    dx=[-1, 0, 1, 0]
    dy=[0, -1, 0, 1]      
    count=0
    queue=deque(q)
    
    while queue:
        grow=queue.popleft()
       
        for i in range(4):  # 주변 토마토 익히기
            xm=grow[0]+dx[i]
            yn=grow[1]+dy[i]
            
            if 0<=xm<m and 0<=yn<n and tomato[xm][yn]==0:
                    tomato[xm][yn]=tomato[grow[0]][grow[1]]+1         # 익힘  
                    queue.append([xm,yn])      # 익은 토마토 큐에 추가해서 다음날에 이용
                    if count < tomato[grow[0]][grow[1]]:
                        count=tomato[grow[0]][grow[1]]              
    if not queue:
        for t in tomato:
            if 0 in t:
                return -1      
        return count
print(bfs())
