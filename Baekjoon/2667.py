# baekjoon 2667 단지번호 붙이기 - dfs
import sys

num=int(input())
dange=[list(sys.stdin.readline().strip()) for i in range(num)]
visit=[[0]*num for i in range(num)]

count=[]    # 각 단지내 집의 수
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

def dfs(x, y):
    visit[x][y]=1
    global number
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<num and 0<=yy<num:
            if visit[xx][yy]==0 and dange[xx][yy]=='1':
                number+=1
                dfs(xx, yy)
            
    
for x in range(num):
    for y in range(num):
        if visit[x][y]==0 and dange[x][y]=='1':
            number=1
            dfs(x, y)
            count.append(number)
            
    
print(len(count))
for i in sorted(count):
    print(i)
