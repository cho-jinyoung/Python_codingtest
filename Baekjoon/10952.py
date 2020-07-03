# 입력은 여러 개의 테스트 케이스로 구성, 각 테스트 케이스는 한 줄로 이루어져 있으며 각 줄에 A와 B 입력, 입력의 마지막에는 0 두개 (0 < A, B < 10)
# 각 테스트 케이스마다 한줄씩 A+B 출력

addlist=[]

while True:
    a,b=input().split( )
    c=int(a)+int(b)
    
    if c==0:
        break;
    addlist.append(c);

for k in addlist:
    print(k)
