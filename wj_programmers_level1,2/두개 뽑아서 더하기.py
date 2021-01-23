def solution(numbers):
    answer = []
    ans_set = set()
    
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            ans_set.add(numbers[i]+numbers[j])
    
    answer = list(ans_set)
    answer.sort()
    return answer
