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
