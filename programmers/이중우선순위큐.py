#heap문제-deque라이브러리 이용해서 풀이

from collections import deque

def solution(operations):
    answer = deque()
    for oper in operations:
        if oper[0]=='I':
            answer.append(int(oper[2:]))
        else:
            answer=deque(sorted(answer))
            if oper[2:]=='1' and answer:
                answer.pop()
            elif oper[2:]=='-1' and answer:
                answer.popleft()
    if not answer:
        return [0,0]
    return [max(answer), min(answer)]
