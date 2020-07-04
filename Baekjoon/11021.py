# 첫째 줄에 테스트 케이스의 개수 T입력. 다음 각 줄에 테스트 케이스 A, B입력. 공백으로 구분
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력. 테스트 케이스 번호는 1부터 시작

addlist=[]
count=1

n=int(input())

for i in range(n):
    a,b=map(int, input().split( ))
    c=a+b
    
    addlist.append(c);

for k in addlist:
    
    print('Case #%d: '%(count), k)
    count+=1

# import sys
# a = int(sys.stdin.readline())  
#
# for i in range(a):
#    b, c = map(int, sys.stdin.readline().split())
#    print("Case #%d:"%(i+1), b+c)

# -> sys.stdin.readline() = input()과 같은 역할을 하지만 속도가 더 빠름
# ex) 한줄씩 입력받아 리스트에 넣음
# import sys
# n=int(input())
# a=[sys.stdin.readline() for i in range(n)]
# print(a)
