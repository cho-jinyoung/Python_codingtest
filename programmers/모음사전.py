# 완전 탐색 -모음사전
# 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어 중 주어진 word 값은 몇번째 단어인지 return
# 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"
# ex) word="AAAE",	return=10  / word="I", return=1563 / word="EIO", return=1189

import itertools
def solution(word):
    alpha=['A', 'E', 'I', 'O', 'U']
    lists=[]
    sorts=[]

    for i in range(1, 6):
        lists.append(list(itertools.product(alpha, repeat=i)))  # 중복, 순서 가능
        
    for p, per in enumerate(lists): # 중복순열 결과 문자열로 만들기
        for j in range(len(lists[p])):
            sorts.append("".join(per[j]))
            
    sorts=list(set(sorts))  # 중복 문자열 제거
    sorts.sort()    # 몇번째 단어인지 확인하기 위해 정렬

    return sorts.index(word)+1
