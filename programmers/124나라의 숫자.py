# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용
# ex) 1=1, 2=2, 3=4, 4=11, 5=12, 6=14 ... 19=141

# point idea
# 3씩 규칙이 있다는 것에 집중, 3으로 나눠떨어지는 경우 예외가 있음


def solution(n):
    l124=[]

    while(n!=0):
        if n%3==0:
            l124.append(4)
            n=n//3-1
        elif n%3==1:
            l124.append(1)
            n=n//3
        elif n%3==2:
            l124.append(2)
            n=n//3
        
    return ''.join(map(str, reversed(l124)))
    
