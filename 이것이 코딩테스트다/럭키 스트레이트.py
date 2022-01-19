# chapter 3 구현 - 럭키스트레이트

inp=list(map(int, input()))

a=inp[:len(inp)//2]
b=inp[len(inp)//2:]

if sum(a)==sum(b):
    print('LUCKY')
else : print('READY')
  
