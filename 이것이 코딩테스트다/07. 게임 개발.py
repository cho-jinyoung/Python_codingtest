# 이것이 코딩테스트다 -구현 04-4. 게임 개발
# **테스트 케이스를 많이 안 넣어봐서 오류가 있을 수 있음 ㅠㅠ

mx, my=map(int, input('map크기(N x M): ').split(" "))
chx, chy, dir=map(int, input('현재 위치 좌표와 방향(0:북, 1:동, 2:남, 3:서): ').split(" "))

ylist=[]
history=[]
dirmove={0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1, 0)}

stop=0
count=1

for i in range(my): # MAP입력
    list=[]
    list=input('각 줄의 칸 지정(0:육지, 1:바다): ').split(" ")
    ylist.append(list)
print(ylist)

while(stop!=4):
    # 방향 변경
    if dir == 0:    dir=3 
    else:    dir-=1

    now=dirmove.get(dir) # 캐릭터 현재 방향

    if (0>chx+now[0] or chx+now[0]>=mx or 0>chy+now[1] or chy+now[1]>=my): # MAP밖으로 나가는 경우
        stop+=1
        continue

    chnow=(chx+now[0], chy+now[1])
    #print(dir, now, chnow)
    
    if (ylist[chy+now[1]][chx+now[0]])=='0': # 리스트에서 x,y축 확인 잘 해야함
        if chnow not in history:
            history.append((chx, chy)) # 갔던 위치 저장
            chx+=now[0]
            chy+=now[1]
            count+=1
            stop=0
        else:
            stop+=1
    else:
        stop+=1

#print(history)    
print('캐릭터가 방문한 칸의 수:', count)
