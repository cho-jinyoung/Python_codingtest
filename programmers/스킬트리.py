# Summer/Winter Coding(~2018) -스킬트리
# 선행 스킬 순서=skill, 스킬트리 배열=skill_trees, 가능한 스킬트리 개수를 return
# ex) skill="CBD", skill_tress=["BACDE", "CBADF", "AECB", "BDA"],	return=2 ("CBADF", "AECB"만 가능)

# point idea
# 선행 스킬 트리는 수행하면 지우고, 각 스킬트리는 수행한 개수를 세어 모두 수행했으면 가능한 스킬트리이므로 이 개수를 카운팅

def solution(skill, skill_trees):
    result=0        # 가능한 스킬트리 개수
    for tre in skill_trees:     # 각 스킬트리
        count=0
        ski=list(skill)         # 선행 스킬 순서
        
        for tstr in list(tre):  # 각 스킬트리의 스킬이
            if tstr not in ski: # 선행 스킬과 상관 없으므로
                count+=1        # 해당 스킬은 가능 count+1 
                
            elif tstr==ski[0]:  # 선행 스킬 순서대로 있으면 
                ski.pop(0)      # 선행 스킬을 수행했으므로 선행 스킬 지움
                count+=1        # 스킬 수행했으므로 count+1
                
        if count==len(tre):     # 모든 스킬이 가능할 때
            result+=1
    return result 
