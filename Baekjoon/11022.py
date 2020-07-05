# 첫째 줄에 테스트 케이스의 개수 T입력. 다음 각 줄에 테스트 케이스 A, B입력. 공백으로 구분
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B.
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
