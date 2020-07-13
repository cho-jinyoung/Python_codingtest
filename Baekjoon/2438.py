# 2438
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

n=int(input())

for j in range(n):
    for i in range(j+1):
        print('*', end='')
    print('\n', end='')
    
# 2439
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제 하지만, 오른쪽을 기준으로 정렬한 별을 출력

n=int(input())

for j in range(n):
    for i in range(n-j, 1, -1):
        print(' ', end='')
    for i in range(j+1):
        print('*', end='')
    print('\n', end='')
