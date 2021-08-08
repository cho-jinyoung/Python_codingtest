# 이것이 코딩테스트다 -그리디 실전문제 3번 1이 될 때까지

n, k=map(int,input('n, k: ').split())
count=0

while(n!=1):
    if (n%k==0):
        n/=k
        count+=1
    else:
        n-=1
        count+=1
print(count) 
