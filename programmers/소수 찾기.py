# 완전탐색 / 소수찾기
# 한자리 숫자가 적힌 문자열 numbers가 주어졌을 때, 만들 수 있는 소수의 개수 return
# numbers는 0~9까지 숫자이며 길이는 1~7 
# ex) [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있으므로 2 return

import itertools

def solution(numbers):
    numlist=[]
    for s in range(1, len(numbers)+1): # 각 자리수 별로 순열값 생성해서 list에 추가
        numlist=numlist+list(map(''.join, itertools.permutations(numbers, s)))
        
    numlist=list(set(map(int,numlist)))   # 리스트 요소 중복 제거
    
    # 소수 판별
    count=0
    for num in numlist:
        flag=0 # 소수 인지 아닌지 판별을 위해        
        for i in range(2, num):
            if num%i==0 : # 소수가 아닌 경우
                flag=1
                break            
        if flag==0 and num!=0 and num!=1: # 소수인 경우
            count+=1
            
    return count
            
