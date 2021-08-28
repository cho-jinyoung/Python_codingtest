# 정렬 / H-index
# 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
# 논문의 인용 횟수 배열=citations, H-Index값 return

# point idea = h-index는 citations의 요소값과 무관하다
# citations=[30, 40]일 때, 2번 이상 인용된 논문이 2편 이상이고 나머지 논문이 2번이하(0번) 인용되었으므로 h-index=2
# case16. [0, 0, 0]일 때, 0번 이상 인용된 논문이 0편 이상이고 나머지 논문이 0번 이하이므로 h-index=0
# case11. [0, 1, 2]일 때, 1번 이상 인용된 논문이 1편 이상(2)이고 나머지 논문이 1번 이하(1)이므로 h-index=1


def solution(citations):
    citations.sort()
    maxx=0
    for i in range(1, len(citations)+1):            # h편
        count=0        
        for cit in citations:                       # h번 이상 인용된 논문의 개수 카운팅
            if cit>=i: 
                count+=1
        if count>=i:                        # h편 이상(>)=h번 인용           
            maxx=max(maxx, i)               # h의 최대값
    return maxx
