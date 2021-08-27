# 해시 / 전화번호 목록
# 매개변수로 전화번호부에 적힌 전화번호 배열=phone_book에서 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return
# 같은 번호는 중복해서 있지 않음
# ex) ["12","123","1235","567","88"] > False, ["123","456","789"] > True


def solution(phone_book):
    # sort를 하면 바로 뒤에 것만 비교하면 됨, 왜냐하면 어차피 바로 뒤와 같지 않다면 그 다음것과도 맞지 않을 것
    # 그러면 for문 1개로 비교 가능!
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        a=hash(phone_book[i])
        
        stri=phone_book[i+1]
        b=hash(stri[0:len(phone_book[i])])
        
        if a==b:
            return False
        
    return True
    
    # 정확성은 모두 통과하지만 효율성을 모두 실패, for문을 2개 써서 그런 듯
    # 겹치는 개수를 세어야 하는 것이 아니므로 전부다 돌 필요 없음
    '''
    count=0    
    for comp in phone_book:
        a=hash(comp)
        strp=ph[0:len(comp)]
            b=hash(strp)
            if a==b and comp!=ph:
                count+=1
                #print(a, b)
    if count>0:
        return False
    else: return True
    '''
