import sys
input=sys.stdin.readline

n, m=map(int, input().split())
r, c, d=map(int, input().split())
lists=[]

dx=[-1, 0, 1, 0]    # 북(0), 동(1), 남(2), 서(3) 
dy=[0, 1, 0, -1]    # > 북 서 남 동 순서로 돌아야 함 

for _ in range(n):
    lists.append(list(map(int, input().split())))

visited=[[False]*m for _ in range(n)]
visited[r][c]=True

clean=1

while True:
    flag=0
    
    for _ in range(4):
        
        d=(d+3)%4 # 회전
        xx=dx[d]+r
        yy=dy[d]+c

        if 0<=xx<n and 0<=yy<m and lists[xx][yy]==0 and visited[xx][yy]==False:
                visited[xx][yy]=True
                clean+=1
                flag=1
                r=xx
                c=yy
                break
    if flag==0:
        if lists[r-dx[d]][c-dy[d]]==1:    # 뒤가 벽이라면 작동 끝
            print(clean)
            exit(0)
        else:
            r, c=r-dx[d], c-dy[d]
