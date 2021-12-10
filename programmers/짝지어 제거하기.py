# 2017 팁스타운
# 효율성 중요 > stack 방식 이용

def solution(s):
    i=1
    stack=[]
    if len(s)<2 or len(s)%2!=0:
        return 0
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if s[i]==stack[-1]:
                stack.pop()
            else :
                stack.append(s[i])
    
    if len(stack)==0:
        return 1
    return 0
