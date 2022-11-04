# Greedy
# 아이디어 다른 사람꺼 많이 참고,,이게 그리디,,?

# 고속도로를 이동하는 차량의 경로 = routes, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지 = result
# ex) routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]], result = 2

# point)
# routes[i][1]을 기준으로 정렬 > routes[i][0]만을 비교했을 때 앞 배열 카메라 설치 구간(start-end)과 같거나 작지 않으면 새 카메라를 설치해야 함
# 왜냐하면 routes[i][1]은 앞 배열 카메라 설치 구간의 end 보다는 확실히 오른쪽(크다)에 있기 때문에 routes[i][0]만 카메라 구간 내 or 더 왼쪽(작다)에 있으면 카메라를 설치하지 않아도 됨



def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    start, end = routes[0][0], routes[0][1]
    
    for i in range(1, len(routes)):
        if start<routes[i][0] and end<routes[i][0]:
            answer+=1
            start=routes[i][0]
            end=routes[i][1]
    return answer
