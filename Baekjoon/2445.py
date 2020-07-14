# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력

n=int(input())

for j in range(1,n+1):
    for i in range(j):
        print('*', end='')
    for i in range((n-j)*2):
        print(' ', end='')
    for i in range(j):
        print('*', end='')
    print('\n', end='')
    
for j in range(1,n):        
    for i in range(n-j):
        print('*', end='')
    for i in range(j*2):
        print(' ', end='')
    for i in range(n-j):
        print('*', end='')    
    print('\n', end='')
