# 2020 KAKAO BLIND RECRUITMENT

def solution(s):
    count=1
    minn=len(s)
    for i in range(0, len(s)//2):           # 문자열 단위
        lists=[]
        word=s[0:i+1]
        for j in range(i+1, len(s)+1, i+1): # 압축
            if word==s[j:j+i+1]:
                count+=1
            else :
                if count>1:
                    lists.append(str(count)+word)
                else:                       # 1 생략
                    lists.append(word)
                word=s[j:j+i+1]
                count=1
            if (len(s)-j)<=i:               # 남는 문자열
                lists.append(s[j:])
        string=''.join(lists)
        minn=min(minn, len(string))
    return minn
