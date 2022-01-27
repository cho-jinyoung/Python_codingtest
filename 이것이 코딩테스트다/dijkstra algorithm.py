# 간단한 dijkstra 알고리즘 = O(v^2)의 시간 복잡도 (V=노드의 개수)

import sys
input=sys.stdin.readline
INF=int(1e9)


node, line=map(int, input().split())    # [입력] 노드 개수, 간선 개수
start=int(input())                      # [입력] 시작 노드 번호 

graph=[[] for i in range(node+1)]       # 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 생성
visited=[False]*(node+1)                # 방문처리 리스트, 노드 인덱스에 맞춰서 접근하기 위해 +1 개 생성
distance=[INF]*(node+1)                 # 최단 거리 테이블 최대값으로 초기화

for _ in range(line):                   # [입력] 간선 정보 > 그래프 생성 
    a, b, c=map(int, input().split())   # a->b 노드로 가는 간선 거리가 c
    graph[a].append((b, c))             # a노드와 연결된 (b노드, 거리c) 튜플을 리스트에 추가

def get_smallest_node():                # 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 반환
    minn=INF                            # 최단거리 초기화
    index=0                             # 최단거리 노드 인덱스 저장할 변수
    for i in range(1, node+1):          # 노드 1~n 인덱스까지
        if distance[i] < minn and not visited[i]:   # 방문하지 않은 노드 중 현재 간선 보다 짧은 경우
            minn=distance[i]
            index=i
    return index

def dijkstra(start):
    distance[start]=0                   # 시작 노드 간선 거리 초기화, 자기 자신까지의 거리이므로 0
    visited[start]=True                 # 현재 노드 방문처리
    for j in graph[start]:              # 시작 노드의 경우
        distance[j[0]]=j[1]             # 시작 노드와 연결된 노드별 간선 거리 저장
    
    for i in range(node-1):
        now=get_smallest_node()         # 현재 남은 노즈 중 최단거리를 가진 노드 가져옴
        visited[now]=True               # 반환된 노드 방문처리
        for j in graph[now]:            # 현재 노드와 연결된 노드
            cost=distance[now]+j[1]     # 현재 노드까지 최단거리 + 연결된 노드로 가는 거리
            if cost < distance[j[0]]:   # 연결된 노드까지 최단거리보다 짧은 경우 최단거리 갱신
                distance[j[0]]=cost

dijkstra(start)

for i in range(1, node+1):              # [결과] 모든 노드까지의 최단거리 출력
    if distance[i] == INF:              # 최단거리가 없는 경우
        print("Infinity")
    else:                               # 최단거리 출력
        print(distance[i])
