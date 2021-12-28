# 전체를 돌면서 두 공의 무게가 같지 않은 경우만 count
# 이 방법은 for문 중첩이기 때문에 효율성 부분에서 낮은 점수를 받을 수 있음
'''n, m=input('볼링공의 개수 N, 공의 최대 무게 M: ').split()
weight=[int(x) for x in input('').split()]

count=0
    
for i in range(len(weight)):
    for j in range(i, len(weight)):
        if weight[i]!=weight[j]:
            count+=1
            
print(count)   '''     
    
# 조합 모듈을 이용하여 모듈의 요소값이 같지 않은 경우 count
'''from itertools import combinations

n, m=input('').split()
weight=[int(x) for x in input('').split()]

count=0

for a, b in combinations(weight, 2):
    if a!=b:
        count+=1
print(count)'''

# 공의 최대 무게를 이용해 경우의 수 세기
n, m=map(int ,input('').split())
input=[int(x) for x in input('').split()]

weight=[0]*11
count=0

for i in input:
    weight[i]+=1        # 각 무게별 공의 개수

for i in range(1, m+1):
    n-=weight[i]        # 전체 공 개수에서 고를 수 없는 개수(이미 고른) 빼기
    count+=weight[i]*n  
print(count)
