# DFS/BFS -타겟넘버
# 사용할 수 있는 숫자 배열=numbers, 타겟 넘버 target이 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수 return
# ex) numbers=[1,1,1,1,1], target=3일때 return=5

def solution(numbers, target):
    count=0
    def dfs(num, lev):
        nonlocal count
        if lev==len(numbers):
            if target==num:
                count+=1
            return          
        dfs(num+numbers[lev], lev+1)
        dfs(num-numbers[lev], lev+1)    
    dfs(0, 0)    
    return count
