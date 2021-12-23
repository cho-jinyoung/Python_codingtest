group=0
answer=0

n=int(input('모험가의 수: '))
score=list(map(int, input('모험가의 공포도를 공백 기준으로 입력: ').split()))
score.sort()

# 처음 생각했던 방식
# -공포도 리스트가 정렬되어 있으므로 맨 처음 공포도의 수만큼 리스트의 요소를 뺌
#  그 다음 남은 리스트에서 같은 방식으로 반복, 리스트가 비었거나 남은 요소의 수가 요소 최솟값보다 작으면 종료
'''while score:   
    m=score[0]
    for i in range(m):
        if score[0]>m:
            break
        score.pop(0)
    if len(score)<score[0]:
        break
    answer+=1'''

# 정답 알고리즘을 읽고 난 후 다시 작성한 코드 
for i in score:
    group+=1
    if group>=i:
        answer+=1
        group=0

print('group 수:', answer)
