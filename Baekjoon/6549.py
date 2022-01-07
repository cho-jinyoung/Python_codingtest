# beakjoon 6549
# 스택 이용
# 현재 높이가 이전 높이(in stack)보다 낮으면 stack의 값 pop하여 넓이 구함
# 즉 현재 높이가 이전보다 높으면 같이 stack에 추가됨
# test case: 7 3 1 1 1 2 1 / 12 3 2 3 4 5 4 3 2 3 1 1 1

import sys

while True:
    inp=[int(n) for n in sys.stdin.readline().split()]+[0]
    num=inp.pop(0)      # 직사각형의 수 
    
    if num==0:          # 0을 입력하면 종료
        break

    stack=[]
    high=0
    
    for i in range(num+1):
        w=i
        while stack and stack[-1][1]>inp[i]:
            w, h=stack.pop()
            high=max(high, (i-w)*h)
        # stack에 값을 넣을 때 현재의 index를 넣으면 안되고 pop한 index를 넣어야 함!!
        stack.append([w, inp[i]])   
    print(high)
      

# 각 높이별로 연속된 x의 수를 구해서 넓이를 구함 > MAX값 체크
# 이 방법은 시간 초과
'''while True:
    inp=[int(n) for n in input().split()]
    num=inp.pop(0)      # 직사각형의 수 
    
    if num==0:          # 0을 입력하면 종료
        break

    high=0
    for i in range(min(inp), max(inp)+1): # 직사각형 높이
        count=0                           # 연속된 x
        count_m=0                         # 현재 높이 중 연속된 x의 최댓값
        for j in range(num):
            if inp[j]<i:
                count=0
            else:                         # 현재 높이보다 크거나 같으면 연속된 것으로 체크
                count+=1
            count_m=max(count_m, count)
        high=max(high, count_m*i)
    print(high)'''
