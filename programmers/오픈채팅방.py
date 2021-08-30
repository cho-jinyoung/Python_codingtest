# 2019 KAKAO BLIND RECRUITMENT

# point idea -해시처럼 id 이용
# enter, change 인 경우 사용자 고유id, 닉네임 딕셔너리 추가 및 수정
# 관리자 문자열 출력시 필요한 id에 따른 닉네임 가져가서 출력

def solution(record):
    dic={}
    printlist=[]
    
    for rec in record:          # user data구축
        relist=rec.split(" ")
        if relist[0]=='Enter' or relist[0]=='Change':   # 입장/변경한 경우 닉네임 설정
            dic[relist[1]]=relist[2]

    for prin in record:
        relist=prin.split(" ")
        if relist[0]=='Enter':      # 입장
            pstr=dic[relist[1]]+'님이 들어왔습니다.'
            printlist.append(pstr)
        elif relist[0]=='Leave':    # 퇴장
            pstr=dic[relist[1]]+'님이 나갔습니다.'
            printlist.append(pstr)
    return printlist
