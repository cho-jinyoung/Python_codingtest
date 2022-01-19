# chapter4. 구현
# 문자열 재정렬

inp=list(input())
inp=sorted(inp)

summ=0
result=[]

for i in range(len(inp)):
    if inp[i].isdigit():        # isdigit=숫자이면 true, 아니면 false
        summ+=int(inp[i])
    else :result.append(inp[i])
        
print("".join(result)+str(summ))
