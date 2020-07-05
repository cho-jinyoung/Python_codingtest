import sys

n=int(input())
addlist=[]
add=[]

for i in range(n):
    a,b=map(int, input().split( ))
    c=a+b
    addlist.append([a,b,a+b])
    
for i in range(n):
    print("Case #%d:"%(i+1), addlist[i][0], "+", addlist[i][1], "=", addlist[i][2])
