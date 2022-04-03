n, m=map(int, input().split())
visited=[False]*n
array=[]

def dfs(N): # N=현재 자리 수
    if m==N:
        print(" ".join(map(str,array)))
        return 
    for i in range(n):
        if not visited[i]:  # 숫자 i(0~(n-1)까지 중)를 이전에 사용한 적이 없으면 
            visited[i]=True # 사용 처리 (=방문 처리)
            array.append(i+1)   # 1부터 시작이니까
            dfs(N+1)            # 다음 자리 수 
            # 원래 상태로 되돌림
            visited[i]=False    
            array.pop()
dfs(0)   
