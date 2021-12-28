# n-1까지 만들 수 있을 때 입력리스트의 다음 요소로 n을 만들 수 있는지가 핵심 

n=int(input('동전의 개수:'))
coin=[int(x) for x in input().split()]
coin.sort()

minimum=1

for i in coin:
    if minimum<i:
        break
    minimum+=i
    
print(minimum)
