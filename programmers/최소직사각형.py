# 완전탐색
# 명함의 가로/세로 길이를 나타내는 2차원 배열 = sizes
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]], return = 4000
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]], return = 133

def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            sizes[i][0], sizes[i][1]=sizes[i][1], sizes[i][0]
            
    max0, max1=sizes[0][0], sizes[0][1]    
    
    for i in range(len(sizes)):
        max0=max(max0,sizes[i][0])
        max1=max(max1,sizes[i][1])
        
    return max0*max1
