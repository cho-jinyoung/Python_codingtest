# 입력은 알파벳 소문자와 대문자로만 이루어진 단어. 길이는 100을 넘지 않고 길이가 0인 단어는 주어지지 않음
# 입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력

import sys

count=0

word=sys.stdin.readline()

a=list(word)

for i in a:
    print(i, end='')
    
    if count==9 :
        count=0
        print('\n', end='')
    else:    
        count +=1
