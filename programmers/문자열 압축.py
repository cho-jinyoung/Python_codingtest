# 2020 KAKAO BLIND RECRUITMENT

def solution(s):
    count=1             # 압축 단위 문자열 개수 count
    minn=len(s)         # 현재 길이 > 최솟값 구하기 위해
    for i in range(1, len(s)//2+1):         # 문자열 단위 길이
        lists=[]        # 합친 문자열 저장할 리스트
        word=s[0:i]     # 단위 길이만큼 자른 문자열
        for j in range(i, len(s)+1, i):     # 압축 루틴
            if word==s[j:j+i]:              # 압축 문자열
                count+=1
            else :
                if count>1: # 문자열 압축 가능
                    lists.append(str(count)+word)
                else:       # 압축 불가
                    lists.append(word)
                word=s[j:j+i]
                count=1
            if (len(s)-j)<=(i-1):           # 남는 문자열
                lists.append(s[j:])
        string=''.join(lists)
        minn=min(minn, len(string))         # 가장 짧은 문자열 길이
    return minn
