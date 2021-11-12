# Summer/Winter Coding(~2018) - 소수 만들기
# nums배열에 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 수 찾기
# 중복 없음, 3<=len(nums)<=50
# ex) [1,2,7,6,4]	> 4

from itertools import combinations

def solution(nums):
    answer = 0
    even=[]
    odd=[]

    for i in nums:  # 짝수 홀수 나누기
        if(i%2==0):   even.append(i)
        else:         odd.append(i)
            
    for o in odd:   # 홀수가 하나 들어가는 경우
        for e in range(len(even)-1):
            for e1 in range(e+1, len(even)):
                answer+=sosoo(o+even[e]+even[e1])
                
    ol=list(combinations(odd, 3))   # 홀수가 3개 들어가는 경우
    for i in ol:
        answer+=sosoo(i[0]+i[1]+i[2])
    return answer

def sosoo(summ):
    for i in range(2, summ):
        if summ%i ==0:
            return 0
    return 1
