# 2021 카카오 BLIND RECRUITMENT
# 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램.
# - 아이디의 길이는 3자 이상 15자 이하.
# - 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있음.
# - 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없음.


def solution(new_id):
    # 1. 소문자 치환
    id_one=new_id.lower()
    
    # 2. 알파벳 소문자(97~122), 숫자(48~57), 빼기(-=45), 밑줄(_=95), 마침표(.=46)를 제외한 모든 문자 제거
    rm_list=[45, 46, 95]
    id_list=list(id_one)
    id_two=[]

    for j in id_list:
        i=ord(j)        
        if (i >96 and i<123) or (i >47 and i <58) or (i in rm_list):
            id_two.append(j)                 
    
    # 3. 마침표가 2번이상 연속되면 하나로 변경
    rm=[]
    for i in range(len(id_two)-1):
        if ord(id_two[i])==46 and (id_two[i]==id_two[i+1]):
            rm.append(i)
    for i, r in enumerate(rm):
        del id_two[r-i]   

    # 4. 처음이나 끝에 있는 경우 제거        
    if len(id_two)!=0 and ord(id_two[0])==46: 
        del id_two[0]
    if len(id_two)!=0 and ord(id_two[-1])==46: 
        del id_two[-1]
    
    # 5. 빈 문자열이라면 new_id에 "a"대입
    if len(id_two)==0:
        for i in range(3):
            id_two.append("a")
            
    # 6. 길이가 16자 이상이면 15개까지 자르기
    if len(id_two)>15:
        del id_two[15:]
    if ord(id_two[-1])==46: 
        del id_two[-1]
        
    # 7. 길이가 2자 이하이면 마지막 문자를 길이가 3일 될 때까지 반복해서 끝에 붙임
    if len(id_two)<3:
        rpt=id_two[-1]
        for i in range(3-len(id_two)):
            id_two.append(rpt) 

    answer = ''.join(id_two)
    return answer
