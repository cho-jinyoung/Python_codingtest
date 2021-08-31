# 탐욕법(Greedy) /구명보트
# 사람들의 몸무게=people, 구명보트의 무게 제한=limit, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값 return (한번에 최대 2명까지 탑승 가능)
# ex) people=[40, 50, 150, 160], limit=200, return=2

# point idea
# 가장 무거운 사람과 가장 가벼운 사람을 더했을 때 limit보다 크다 -무거운 사람은 무조건 혼자 타야 한다
# left index와 right index가 같다면 한명 남은 경우 -무조건 혼자 타야함
# 효율성을 위해서는 요소에 직접 접근하여 pop하기보다 index를 이동하면서 접근하는 것이 좋다

def solution(people, limit):
    people.sort()
    left, save=0, 0
    right=len(people)-1
    while(left<right):                          # 오른쪽에서 오는 인덱스가 더 큰 경우만 존재
        if limit>=people[left]+people[right]:   # 가장 무거운 사람과 가장 가벼운 사람을 더했을 때 limit보다 작아야 같이 탐
            left+=1
            right-=1 
        elif limit<people[left]+people[right]:
            right-=1
        save+=1
    if left==right:                             # 한명 남은 경우
        save+=1
    return save 
