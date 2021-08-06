# 이것이 코딩테스트다 -그리디 실전문제 1번 큰수의 법칙

n, m, k=input('배열의 크기, 숫자가 더해지는 횟수, 연속 횟수를 순서대로 입력하세요:').split()
data=list(map(int, input().split()))

data.sort()
big=data[n-1]
big2=data[n-2]

count=0
sum=0

while(count!=m): # 전체 숫자 횟수
    for j in range(k): # 연속으로 올 수 있는 횟수
        sum+=big
        count+=1
    sum+=big2
    count+=1

print (sum)
