# n이 주어졌을 때, 1부터 n까지 합 (1 ≤ n ≤ 10,000)

n=int(input())

all_sum=0

for i in range(n+1):
    all_sum += i
print(all_sum)
