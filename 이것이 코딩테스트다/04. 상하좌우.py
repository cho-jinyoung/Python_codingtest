# 이것이 코딩테스트다 -구현 04. 상하좌우

n=input('공간의 크기(NxN): ')
plan=list(map(str, input().split()))

dic={ 'L':[0, -1], 'R':[0, 1], 'U':[-1, 0], 'D':[1, 0] }
list=[]
zero=[1, 1]

for p in plan:
    list=[x+y for x, y in zip(zero, dic[p])]
    if 0 in list:
        continue
    zero=list
print(zero)
