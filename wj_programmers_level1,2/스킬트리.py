def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        s_list = [] # skill을 제외한 알파벳 제거 -> slist에 저장
        for st in skill_tree:
            if st in skill:
                s_list.append(st) # 이렇게 넣으면은 순서가 반대로 됨. 이걸 이용하여 pop을 쓰자
        
        #s_list = list(set(s_list)) # 중복되는 스킬 제거. 일단 중복 신경쓰지말아보자. set하면 순서가 뒤바뀌어서 매번 결과가 달라짐
        #### 중복 신경 안써도 되는 문제였다.
        
        # skill 순서 처리
        flag = True
        for i in range(0, len(s_list)):
            if s_list[i] != skill[i]:
                flag = False
        if flag == True:
            answer +=1
            
    return answer
