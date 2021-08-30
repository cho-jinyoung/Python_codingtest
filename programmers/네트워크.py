# DFS/BFS -네트워크
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현 (computer[i][i]는 항상 1)
# ex) n=3, computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]], return=2

def dfs(node, visited, computers, n):
    visited[node]=True                                  # 현재 노드 방문 체크
    for i in range(n):
        if computers[node][i]:                          # 현재 노드와 연결된 노드이면
            computers[node][i], computers[i][node]=0,0  # 한번 갔던 곳 지움
            dfs(i, visited, computers, n)               # 현재 노드와 연결된 네트워크를 노드로 하여 연결 확인

def solution(n, computers):   
    count=0
    visited=[False]*n                       # 모두 방문하지 않은 노드로 초기화
    
    for i in range(n):
        if visited[i]==False:               # 방문하지 않은 노드이면
            dfs(i, visited, computers, n)   # i 노드와 연결된 네트워크 모두 방문 
            count+=1                        # 연결된 네트워크 1개 카운팅
    return count   
