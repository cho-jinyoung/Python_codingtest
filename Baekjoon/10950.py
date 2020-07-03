# 첫째 줄에 테스트 케이스의 개수 T, 다음 각 줄에 A와 B를 입력하면 
# 각 케이스마다 A+B 의 값을 출력 (0 < A, B < 10)

count=int(input())
s=[]
for i in range(count):
    a,b=input().split( )
    s.append((a,b))
for (f,l) in s:
    print(int(f)+int(l))
