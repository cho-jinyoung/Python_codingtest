# BFS/DFS
# 게임 맵 최단거리
# 0(갈수없음)과 1(갈수있음)으로 이루어진 행렬 maps이 매개변수 일때 (n,m)에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return
# 단 도착할 수 없을 때는 -1 return
# 시작 위치는 (1,1)

# ex) maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]], return = 11

from collections import deque

def bfs(maps, queue):
    dx, dy=(0, 1, 0, -1), (1, 0, -1, 0) # 사방으로 갈 수 있는 방법
    while queue:                        # queue가 존재하는 동안
        now=queue.popleft()             # 현재 위치
        if (now[0]==(len(maps)-1) and now[1]==(len(maps[0])-1)) : # 도착지에 도달한 경우
            return now[2]
        for i in range(4):
            nx, ny=now[0]+dx[i], now[1]+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1:  # 맵을 벗어나지 않으면서 갈 수 있는(1) 길
                maps[nx][ny]=0                    # 한번 갔던 길에 다시 갈 수 없도록 (효율성을 위해 핵심인 부분****)
                queue.append((nx, ny, now[2]+1))  # 한칸 이동
    return -1
def solution(maps):
    queue=deque([(0,0,1)])    # 시작위치
    return bfs(maps, queue)

# 어려워서 한번 더 풀었당
# 1. 이미 지나온 길은 1로 visit 체크
# 2. 칸 밖으로 나가는 경우 / 해당 칸의 visit값이 0인 경우 / 해당 칸의 visit값이 1인 경우-방문처리
# 3. 가장 최단거리에 먼저 도착해서 return 되므로 더 긴 경우는 생각하지 않아도 됨
# 4. x, y 헷갈림 주의!!!
# 5. 방문처리를 큐에 넣을때 해야함, 큐에서 꺼낼 때 하게 되면 중복으로 큐에 넣는 경우가 생길 수 있음
'''
from collections import deque

def bfs(maps, que):
    # direct=완료지점에 더 가까운 곳 부터 확인하도록 순서를 지정함
    direct=[[1,0],[0,1],[-1,0],[0,-1]]  # x, y
    while que:
        q=que.popleft()      # 더 가까운 곳 부터 해야 최단거리
        if (len(maps[0])-1)==q[1] and (len(maps)-1)==q[0]:
            return q[2]       # 가장 최단거리 리턴
        for dic in direct:    # 각 방향 별로
            ax=q[0]+dic[0]    # x
            ay=q[1]+dic[1]    # y
            if len(maps)>ax>-1 and len(maps[0])>ay>-1 and maps[ax][ay]==1:
                maps[ax][ay]=0   # 지난 곳 다시 지나지 않도록 방문처리
                que.append([ax, ay, q[2]+1])    
    return -1   # que를 다 돌아도 끝까지 도달하지 못하는 경우
            
def solution(maps):
    que=deque([(0,0,1)])    # (x, y, visit count)
    return bfs(maps, que)
'''
