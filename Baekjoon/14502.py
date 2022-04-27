# beakjoon 14502
# brute force + BFS
# 벽을 세우고 2의 확장 범위 체크

from collections import deque
import sys
import copy
input=sys.stdin.readline

x,y=map(int, input().split())
lists=[]
                 
zeroque=deque()
virusque=deque()

maxzero=0

# 바이러스 전파 (BFS)
def virus():
    global maxzero    
    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]

    temp=copy.deepcopy(lists)
    que=copy.deepcopy(virusque) # 복사를 안하면 기존 바이러스 위치까지 pop !!
                    
    while que:
        qxy=que.popleft()
        for i in range(4):
            ax=qxy[0]+dx[i]
            ay=qxy[1]+dy[i]
            if 0<=ax<x and 0<=ay<y and temp[ax][ay]==0:
                temp[ax][ay]=2
                que.append([ax, ay])
                            
    # 안전 영역 크기
    zero=0
    for i in range(x):
        zero+=temp[i].count(0)
    maxzero=max(zero, maxzero)
            
for xx in range(x):   # 입력 + 바이러스 위치, 정상 위치 파악
    lis=list(map(int, input().split()))
    for yy in range(y):
        if lis[yy]==0:
            zeroque.append([xx, yy])
        if lis[yy]==2:
            virusque.append([xx, yy])
    lists.append(lis)
    
for a in range(len(zeroque)): # *** brute force ***
    for b in range(a):
        for c in range(b):
            c0, c1=zeroque[c]
            b0, b1=zeroque[b]
            a0, a1=zeroque[a]

            lists[c0][c1]=1
            lists[b0][b1]=1
            lists[a0][a1]=1
            virus()
            lists[c0][c1]=0
            lists[b0][b1]=0
            lists[a0][a1]=0
            
print(maxzero)
