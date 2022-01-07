# beakjoon 2304
# 가장 높은 기둥을 찾음, 양쪽으로 그 기둥 이후에 낮은 기둥을 찾음 > 반복

import sys 

N=int(sys.stdin.readline())  # 기둥의 개수

max_x, max_y=0, 0
high=[0]*1001

for i in range(N):
    x, y=(map(int, sys.stdin.readline().split()))
    max_x=max(max_x, x)     # 기둥 위치
    max_y=max(max_y, y)     # 기둥 높이
    high[x]=y

for i in range(max_x+1):    # 가장 높은 기둥 index
    if max_y==high[i]:
        index=i
        break

summ=max_y
maxx=high[0]
for i in range(index):  # 가장 높은 높이의 left
    maxx=max(maxx, high[i])
    summ+=maxx

maxx=high[max_x]
for i in range(max_x, index, -1):   # 가장 높은 높이의 right
    maxx=max(maxx, high[i])
    summ+=maxx  
print(summ)
