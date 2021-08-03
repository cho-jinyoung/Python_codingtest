# 2021 Dev-Matching: 웹 백엔드 개발자

# 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 
# 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정

# - lottos는 길이 6인 정수 배열. 모든 원소는 0 이상 45 이하인 정수.
# - 0은 알아볼 수 없는 숫자를 의미하며 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않음.
# - win_nums은 길이 6인 정수 배열. 모든 원소는 1 이상 45 이하인 정수.
# - win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
# - lottos, win_nums의 원소들은 정렬되어 있지 않을 수도 있음.

def solution(lottos, win_nums):
    rank={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    lottos.sort()
    win_nums.sort()
    
    count=0
    zero=0
    answer = []
    
    for i in lottos:
        if i==0:
            zero+=1
        for j in win_nums:
            if i==j:
                count+=1
    #print(zero, rank.get(count+zero), rank.get(count))
    answer.append(rank.get(count+zero))
    answer.append(rank.get(count))
    return answer
