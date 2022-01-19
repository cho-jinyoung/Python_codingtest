# chapter 5 DFS/BFS
# 음료수 얼려먹기 > DFS

import sys

def dfs(ice, a, b):
    direct=[(0,1), (0,-1), (1, 0), (-1, 0)]
    if a<0 or a>=n or b<0 or b>=m:  # 범위를 벗어나는 경우
        return False
    if ice[a][b]==0:
        ice[a][b]=1
        for i in direct:  # 각 방향 체크
            dfs(ice, a+i[0], b+i[1])
        return True
        
n, m=map(int, sys.stdin.readline().split())

ice=[]
for i in range(n):
    ice.append(list(map(int, input())))
    
count=0    

for a in range(n):      # 모든 노드를 체크 
    for b in range(m):
        if dfs(ice, a, b)==True:
            count+=1
print(count) 
