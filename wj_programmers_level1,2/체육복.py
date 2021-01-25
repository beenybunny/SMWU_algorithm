# 반례 모두 통과하는데 testcase6 통과를 못한다. 왜지

def solution(n, lost, reserve):
    # 제한사항 5번. lost와 reserve 중복되는 사람은 두 리스트에서 제거
    for l in range(0, n):
        if l in reserve and l in lost:
            reserve.remove(l)
            lost.remove(l)
            
    answer = n - len(lost) # 초기 answer 
    
    for l in lost:
        if l-1 in reserve: # 앞에 빌려줄 수 있는 여벌옷 있으면,
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve: # 뒤에 빌려줄 수 있는 여벌옷 있으면,
            reserve.remove(l+1)
            answer += 1
        
    return answer
