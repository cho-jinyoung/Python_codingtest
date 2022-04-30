# beakjoon 14889
# 구현
# 두 팀으로 나눠서 리스트 만들고, for 돌려서 그 리스트의 능력치를 합함

import sys
from itertools import combinations

input=sys.stdin.readline

n=int(input())
lists=[]
minn=10000

for _ in range(n):
    lists.append(list(map(int, input().split())))

startlink=list(combinations(range(n), n//2))
ateam=startlink[:len(startlink)//2]
bteam=startlink[len(startlink)//2:]

    
for i in range(len(ateam)):
    ascore, bscore=0, 0

    ascorelist=list(combinations(ateam[i], 2))
    bscorelist=list(combinations(bteam[(len(bteam)-1)-i], 2))

    for k, l in zip(ascorelist, bscorelist):
        ascore+=lists[k[0]][k[1]]+lists[k[1]][k[0]] 
        bscore+=lists[l[0]][l[1]]+lists[l[1]][l[0]]

    minn=min(minn, abs(ascore-bscore))    

print(minn)
