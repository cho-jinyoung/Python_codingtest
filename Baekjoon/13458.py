# beakjoon 13458
import sys
input=sys.stdin.readline

N=int(input())
An=list(map(int, input().split()))
b, c=map(int,input().split())
count=0

for i in range(len(An)):
    An[i]-=b
    count+=1

    if An[i]>0:
        count+=An[i]//c
        An[i]-=(An[i]//c)*c

        if An[i]>0:
            count+=1            
print(count)
