# 8393번
# n이 주어졌을 때, 1부터 n까지 합 (1 ≤ n ≤ 10,000)

n=int(input())

all_sum=0

for i in range(n+1):
    all_sum += i
print(all_sum)

# 10818번
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000), 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어짐

n=int(input())

nlist=list(map(int,input().split( )))
print(max(nlist),min(nlist))
