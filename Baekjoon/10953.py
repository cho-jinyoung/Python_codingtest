# 첫째 줄에 테스트 케이스의 개수 T입력, 다음 각 줄에 테스트 케이스 A, B를 콤마(,)로 구분하여 입력
# 각 테스트 케이스마다 A+B 출력

addlist=[]
n=int(input())

for i in range(n):
    a,b=map(int, input().split(','))
    c=a+b
    # a,b=input().split(',')
    # c=int(a)+int(b)
    
    addlist.append(c);

for k in addlist:
    print(k)
