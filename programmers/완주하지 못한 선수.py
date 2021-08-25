# 완주하지 못한 선수
# 마라톤에 참여한 선수=participant, 완주한 선수=completion 배열이 주어질 때, 완주하지 못한 선수의 이름을 return
# 동명이인이 있을 수 있음
# ex) participant=["mislav", "stanko", "mislav", "ana"], completion=["stanko", "ana", "mislav"], return="mislav"
def solution(participant, completion):
      
# 처음 풀이 > 효율성 테스트 실패
# 처음엔 아래 주석코드로 짰는데 시간복잡도를 생각하지 않아 효율성 부분에서 점수를 받지 못했다
    '''
    for i in participant:
        a=participant.count(i)
        b=completion.count(i)
            
        if a!=b:
            return i
    '''
    
# 1번 정답
    '''
    participant.sort()
    completion.sort() # 정렬하면 시간이 조금 빨라짐 
    
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
    '''
    
# 2번 정답 > 해시 이용    
    p_hash={}
    part=0
    
    for i in participant:
        p_hash[hash(i)]=i
        part+=hash(i)
    for i in completion:
        part-=hash(i)
        
    return p_hash[part]
