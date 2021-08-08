# 이것이 코딩테스트다 -그리디 실전문제 2번 숫자 카드 게임

a,b=input('행x열: ').split()
result=0

for i in range(int(a)):
    duf=list(map(int, input().split()))
    if (result < min(duf)):
        result=min(duf)
        
print (result)
