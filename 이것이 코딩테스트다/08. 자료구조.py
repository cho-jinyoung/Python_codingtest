# 이것이 코딩테스트다 -DFS 01.자료구조

# stack (선입후출)
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(3)
stack.append(4)
stack.pop()

print("stack:", stack)

# queue (선입선출)
from collections import deque

queue=deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(2)
queue.append(1)
queue.popleft()

print("queue 먼저 들어온 순서:", queue)
queue.reverse()
print("queue 나중에 들어온 순서:", queue)

# 재귀함수 -팩토리얼 예제

n=int(input("N:"))

def factorial(n):
    if n==1:
        return 1
    return factorial(n-1)*n

print(factorial(n))
