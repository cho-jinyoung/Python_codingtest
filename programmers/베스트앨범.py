# 장르 전체 재생 횟수 순서 - 장르 내 많이 재생된 순서대로 2개 pick
def solution(genres, plays):
    answer = []
    v_sort=[]
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            # 장르가 dic에 있으면 장르 전체 횟수 누적합과 각 노래 횟수 저장
            dic[genres[i]].append([plays[i], i])
            dic[genres[i]][0]+=plays[i]
        else:
            # 장르가 dic에 없으면 장르 전체 횟수 누적합을 구하기 위한 첫번째 변수와 각 노래 횟수 저장
            dic[genres[i]]=[plays[i], [plays[i], i]] 
    
    for d, v in sorted(dic.items(), key=lambda x:x[1][0], reverse=True):
        v.pop(0)    # 누적합 제외하고 sort
        v.sort(reverse=True)
        
        if len(v)>1:
            if v[1][0]==v[0][0]:        # 재생 횟수가 같은 경우 고유번호가 낮은 노래 먼저
                answer.append(v[1][1])
                answer.append(v[0][1])
            else:
                answer.append(v[0][1])
                answer.append(v[1][1])
        else:   # 장르에 노래가 하나인 경우
            answer.append(v[0][1])
            
    return answer
