# beakjoon 15650

n, m=map(int, input().split())
visit=[True]*n
suyal=[]
global bigger
bigger=0

def dfs(N): # N = 현재 자리 수
    global bigger
    if N==m:
        print(" ".join(map(str, suyal)))
        return
    for i in range(n):
        if visit[i] and bigger<(i+1):
            visit[i]=False
            suyal.append(i+1)
            bigger=i+1
            dfs(N+1)    # 다음 자리수
            # 원래 상태로 되돌림 (백트래킹)
            visit[i]=True
            if len(suyal)-1!=0: # 이게 최선이 아닐 것 같은데...
                bigger=suyal[N-1]
            suyal.pop()
dfs(0)  
