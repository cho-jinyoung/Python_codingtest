x=int(input())
star=1
for i in range(x, 0, -1):
    for j in range(i-1, 0, -1):
        print(' ',end='')
    for k in range(star):
        print('*',end='')
    star=star+2
    print("");