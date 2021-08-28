# 완전 탐색 / 카펫
# 노란색 격자를 갈색 격자가 둘러싸고 있는 모양에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return (가로>=세로)

# point idea
# yellow의 가로+2 = brown의 가로
# brown+yellow=answer[0]*answer[1]
# answer[0]>=answer[1]


def solution(brown, yellow):
    yelist=[]
    
    for i in range(1, yellow+1):            # 안쪽 yellow크기가 될 수 있는 경우 (가로 * 세로) =약수
        ap=[i]
        if yellow%i==0 and i>=(yellow//i):  # 약수 중 첫번째 수가 두번째 수보다 큰 경우만 
            ap.append(yellow//i)
            yelist.append(ap)  

    for yel in yelist:             
        if (brown+yellow)%(yel[0]+2)==0:    # 전체 크기가 될 수 있는 수 중에 첫번째 약수+2의 값을 약수로 가지는 값
            answer=[yel[0]+2, (brown+yellow)//(yel[0]+2)]
    return answer

            
