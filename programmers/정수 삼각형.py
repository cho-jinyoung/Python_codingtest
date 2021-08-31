# DP /정수 삼각형 
# 삼각형의 정보가 담긴 배열=triangle, 거쳐간 숫자의 최댓값 return
# triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], return=30

# point idea
# 예외 경우인 맨 첫번째수, 맨 마지막수는 바로 위의 값만 더할 수 있으므로 따로 지정하고, 중간의 값은 더 큰 수를 누적으로 더하도록 함
# 맨 마지막 층까지 그 자리에 누적 합을 저장하여 마지막 층 배열중 가장 큰 수를 뽑으면 됨

def solution(triangle):
    for row in range(1, len(triangle)):                 # 삼각형의 각 층
        for k in range(row+1):                          # 한 층의 모든 값에 접근해 누적합 계산
            if k==0:                                    # 맨 왼쪽 수인 경우
                triangle[row][k]+=triangle[row-1][k]
            elif k==row:                                # 맨 오른쪽 수인 경우
                triangle[row][k]+=triangle[row-1][row-1]
            else:                                       # 가운데 수인 경우
                triangle[row][k]+=max(triangle[row-1][k-1], triangle[row-1][k]) # 위 층의 인접한 수 중에 큰 수를 더함
    return max(triangle[-1])                            # 맨 아래층의 가장 큰 수 출력
