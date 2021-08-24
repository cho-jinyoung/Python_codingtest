# 2021 카카오 채용연계형 인턴십
# 숫자 문자열의 일부가 영단어로 바뀌어졌거나 그대로인 문자열 s가 입력으로 주어짐.
# 문자열 s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성.
# - 1 <= len(S) <= 50
# - "zero" 또는 "0"으로 시작하는 경우는 없음
# - return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어짐
# - 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,'eight':8,'nine':9

def solution(s):
    s=s.lower()
    slist=list(s)
    
    dic={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,'eight':8,'nine':9}
    ori=[]          # 모두 숫자로 바꾼 리스트 즉 출력에 해당
    intstring=[]    # 문자열 완성을 위해 사용하는 리스트 -매번 초기화 필요
    
    for i in slist:
        if 0x2F<ord(i) and ord(i)<0x3A :  # 숫자인 경우
            ori.append(i)                 # 출력 리스트에 현재 숫자 추가
            
            joint="".join(intstring)      # 숫자 나오기 전까지의 문자열 완성
            
            if joint in dic: 
                dicval=dic[joint]
                ori.append(dicval)
                ori.append(joint)
            intstring=[]
            joint=[]
            
        else:  #연속으로 문자인 경우
            intstring.append(i)       # 문자열에 문자 하나 추가, 이 문자열은 계속 바뀔 것
            joint="".join(intstring)  # joint도 계속 바뀌는 변수, 리스트를 문자열로
            
            if joint in dic:        # 문자열이 완성되면
                dicval=dic[joint]   # 딕셔너리에서 문자열에 해당하는 value찾음
                ori.append(dicval)  # 출력 리스트에 추가
                intstring=[]
            
    answer = "".join(str(i) for i in ori) # 리스트에 int 타입인 요소를 str로 형변환하고 한문자열로 합침 
    
    return int(answer) # 문자열이 str타입이므로 int로 형변환
