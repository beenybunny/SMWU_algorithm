import pdb

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skill_idx = 0
        breaker = False
        
        #pdb.set_trace()

        for i in tree:
            new_idx= skill.find(i)
            if new_idx != -1:
                if new_idx == skill_idx:
                    skill_idx+=1
                else: #이전 스킬을 배우지 않은 경우
                    breaker = True
                    break 
        if not breaker :
            print(tree)
            answer+=1
    return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])
