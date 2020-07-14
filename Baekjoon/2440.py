# 2440번
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

n=int(input())

for j in range(n,0,-1):
    for i in range(j):
        print('*', end='')
    print('\n', end='')
    
# 2441번
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제, 다만 오른쪽 정렬

n=int(input())

for j in range(n,0,-1):
    for i in range(n-j):
        print(' ', end='')
    for i in range(j):
        print('*', end='')
    print('\n', end='')
