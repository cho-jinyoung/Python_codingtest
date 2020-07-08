# 입력은 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100), 둘째 줄에 숫자 N개 공백없이 입력
# 입력으로 주어진 숫자 N개의 합을 출력

sum=0

n=int(input())

num=input()
a=list(num) #한글자씩 끊어서 리스트에 넣기

for i in range(n):
    sum=sum+int(a[i])

print(sum)
