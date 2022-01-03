# beakjoon 5397 키로거
# 커서를 움직이는 구현 방식 > 시간 복잡도 증가
# 따라서 커서를 가운데 두었다고 생각하고 양쪽 리스트에 값을 이동시킴

from sys import stdin
n=int(input())

for k in range(n):
    password=stdin.readline().strip()
    left, right=[], []
    
    for val in password:
        if val=='<':
            if left:
                right.append(left.pop())
        elif val=='>':
            if right:
                left.append(right.pop())
        elif val=='-':
            if left:
                left.pop()
        else:
            left.append(val)

    print("".join(left)+"".join(reversed(right)))
