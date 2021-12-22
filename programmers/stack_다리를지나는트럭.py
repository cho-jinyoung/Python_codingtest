# 다리에 올라갈 수 있는 트럭 수 = bridge_length, 다리가 견딜 수 있는 무게 = weight, 트럭 별 무게 = truck_weights
# ex) 100	100	[10,10,10,10,10,10,10,10,10,10]	 >  110
# ex) 2	10	[7,4,5,6]	 >  8

def solution(bridge_length, weight, truck_weights):
    answer=0
    stack=[0]*bridge_length
    
    while stack:
        answer+=1
        stack.pop(0)
        if truck_weights:
            if sum(stack)+truck_weights[0]<=weight:
                stack.append(truck_weights.pop(0))
            else:
                stack.append(0)
    return answer
