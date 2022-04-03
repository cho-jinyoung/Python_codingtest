n, m=map(int, input().split())
visited=[False]*n
array=[]

def dfs(N):
    if m==N:
        print(" ".join(map(str,array)))
        return 
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            array.append(i+1)   # 1부터 시작이니까
            dfs(N+1)            # 다음 자리 수 
            visited[i]=False
            array.pop()
dfs(0)   
