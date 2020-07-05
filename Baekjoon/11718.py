# 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 
# 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.
# 입력 그대로 출력

# case 1. input 이용
while True:
  try:
    print(input())
  except EOFError:
    break

# case 2. readline 이용
import sys
while True:
    line=sys.stdin.readline()
    if not line: 
        break
    print(line, end='')
    # readline은 마지막에 \n이 들어가기 때문에 end=''를 사용하여 없애줌
