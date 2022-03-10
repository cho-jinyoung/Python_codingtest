# 디스크 컨트롤러
# 힙 부분 문제인데 힙을 이용하진 않음..
# 현재 시점에서 시간(작업 요청부터 종료까지=answer)이 가장 적은 작업을 그때그때 정렬을 통해 찾아서 값을 계산

def solution(jobs):
    l=len(jobs)
    jobs=sorted(jobs, key = lambda x: (x[0], x[1]))

    answer=jobs[0][1]           # 작업 요청부터 종료까지 시간
    task=jobs[0][0]+jobs[0][1]  # 이전 작업 종료 시간
    jobs.pop(0)                 # 작업 진행 완료 후 삭제

    while jobs:
        ind=[i for i, val in enumerate(jobs) if val[0]<=task] # 이전 작업 종료 시간이내에 들어온 작업의 최대 인덱스 구함

        if ind:     # 이전 작업 종료 시간 이내에 들어온 작업이 있는 경우
            jobs[:ind[-1]+1]=sorted(jobs[:ind[-1]+1], key=lambda x:x[1])
            task=task+jobs[0][1]
            answer=answer+task-jobs[0][0]
        else:       # 이전 작업 종료 시간 이후에 들어온 작업만 존재하는 경우
            jobs=sorted(jobs, key=lambda x:x[1])
            task=jobs[0][0]+jobs[0][1]
            answer+=jobs[0][1]
            
        jobs.pop(0)     # 요청 완료 후 삭제
        
    return answer//l    # 평균
