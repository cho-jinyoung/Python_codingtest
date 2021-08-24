# 완주하지 못한 선수
# 마라톤에 참여한 선수=participant, 완주한 선수=completion 배열이 주어질 때, 완주하지 못한 선수의 이름을 return
# 동명이인이 있을 수 있음
# ex) participant=["mislav", "stanko", "mislav", "ana"], completion=["stanko", "ana", "mislav"], return="mislav"
def solution(participant, completion):
    # 처음엔 아래 주석코드로 짰는데 시간복잡도를 생각하지 않아 효율성 부분에서 점수를 받지 못했다
    '''    
    for i in participant:
        a=participant.count(i)
        b=completion.count(i)
            
        if a!=b:
            return i
    '''
    # 아래 코드의 시간복잡도는 O(n)
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)-1): # 정렬한 리스트의 처음-중간 부분에 완주하지 못한 선수의 이름이 있는 경우
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1] # 정렬한 리스트의 맨 마지막에 완주하지 못한 선수의 이름이 
