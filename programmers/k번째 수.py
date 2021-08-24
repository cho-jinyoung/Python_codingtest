# 
# array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수
# ex) array=[1, 5, 2, 6, 3, 7, 4],	commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]],	return=[5, 6, 3]

def solution(array, commands):
    
    com_sl=[]
    answer = []
    
    for i in range(len(commands)):
        com_sl=array[commands[i][0]-1:commands[i][1]]
        com_sl.sort()
        answer.append(com_sl[commands[i][2]-1])
    
    return answer
