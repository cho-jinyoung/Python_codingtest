# 탐욕법(greedy) /체육복
# 전체 학생=n, 체육복 없는 학생 배열=lost, 여벌을 가진 학생 배열=reserve가 주어질 때, 수업 들을 수 있는 학생의 최댓값 return 
# ex) n =7, lost =[1, 2, 3, 4, 5, 6, 7], reserve =[1, 2, 3], return =3

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in range(1, n+1):
        if i in reserve and i in lost:    # 도난당한 학생이 여유분을 가진 경우
            lost.remove(i)
            reserve.remove(i)

    losts=lost[:] # 그냥 요소를 remove하면 for문에서 리스트가 줄어 오류가 생겼음

    for i in lost:
        if (i-1) in reserve: # 앞 사람에게 빌리는 경우 (정렬했으므로 앞사람에게 먼저 빌려야 함)
            losts.remove(i)
            reserve.remove(i-1)
        elif (i+1) in reserve: # 뒷 사람에게 빌리는 경우
            losts.remove(i)
            reserve.remove(i+1)
    return n-len(losts)
    
