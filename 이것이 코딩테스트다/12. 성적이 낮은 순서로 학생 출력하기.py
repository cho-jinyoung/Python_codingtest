# chapter 6 정렬
# 성적이 낮은 순서로 학생 출력하기

import sys

n=int(sys.stdin.readline())

stu={}
for i in range(n):
    a, b=sys.stdin.readline().split()
    stu[a]=int(b)

stu=sorted(stu.items(), key=lambda x:x[1])

for i in range(n):
    print(stu[i][0], end=" ")
