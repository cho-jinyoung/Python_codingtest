# chapter 6 정렬
# 위에서 아래로

import sys

n=int(sys.stdin.readline())

inp=[]
for i in range(n):
    inp.append(int(sys.stdin.readline()))

inp.sort(reverse=True)

for i in range(n):
    print(inp[i])
