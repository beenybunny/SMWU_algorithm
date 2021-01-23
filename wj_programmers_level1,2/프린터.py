def solution(priorities, location):
    answer = 0
    
    while True:
        m = max(priorities)
        front = priorities.pop(0) # dequeue를 이용하여 효율성 up
        
        if m == front:
            if location == 0: # 지금 프린트되는 최댓값이 location이므로 answer 반환
                break
            else:
                answer += 1 # 맨 앞에꺼 프린트되므로 answer+1
                location -= 1 # 맨 앞에 하나 없어지니까 한칸씩 땡김
                
        elif m != front:
            if location == 0:
                priorities.append(front) # front는 맨 뒤에 추가
                location = len(priorities)-1 # location도 맨뒤로 조정
            else:
                priorities.append(front)
                location -= 1
                
    return answer+1
