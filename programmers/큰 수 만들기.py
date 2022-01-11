# [i]<[i+1]이면 stack pop > [i+1] push
# [i]>=[i+1]이면 [i+1] push
def solution(number, k):
    stack=[]
    for num in number:
        if not stack:
            stack.append(num)
            continue
        if k>0:
            while stack[-1]<num:
                stack.pop()
                k-=1
                if not stack or k<=0:
                    break    
        stack.append(num)
    
    stack = stack[:-k] if k > 0 else stack

    return "".join(stack)
