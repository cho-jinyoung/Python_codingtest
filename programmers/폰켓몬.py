# 해시
# N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법
# ex) nums=[3,1,2,3], result=2 / nums=[3,3,3,2,2,4], result=3 / 

def solution(nums):
    distinc=list(set(nums))
    if len(distinc)>len(nums)//2:
        return len(nums)//2
    else:
        return len(distinc)
    
    # 더 간단한 코드..
    #return min(len(list(set(nums))), len(nums)//2)
