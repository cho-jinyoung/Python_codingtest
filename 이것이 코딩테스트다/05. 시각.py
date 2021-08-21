# 이것이 코딩테스트다 -구현 04-2. 시각

# N이 입력되면 00시00분00초 - N시59분59초까지의 모든 시각중에 3이 하나5라도 포함되는 경우의 수

n=input('시: ')
count=0

for i in range(int(n)+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)
