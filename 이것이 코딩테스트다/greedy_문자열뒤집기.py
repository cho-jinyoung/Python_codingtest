import math

inputS=input('0과 1로만 이루어진 문자열 입력: ')
listS=list(inputS)
count=0

# 앞의 숫자와 같지 않은 부분의 수 // 2
for i in range(1, len(listS)):
    if listS[i-1]!=listS[i]:
        count+=1
print(math.ceil(count/2))
