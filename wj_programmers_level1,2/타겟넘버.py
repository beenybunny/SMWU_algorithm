def dfs(prev, index, numbers, target):
    if index >= len(numbers):
        if target == prev:
            return 1
        else:
            return 0
    
    cur1 = prev + numbers[index]
    cur2 = prev - numbers[index]
    
    ans = 0
    ans += dfs(cur1, index+1, numbers, target)
    ans += dfs(cur2, index+1, numbers, target)
    return ans

def solution(numbers, target): # dfs. 재귀 이용.
    answer = 0
    cur = numbers[0]
    answer += dfs(cur, 1, numbers, target)
    answer += dfs(-cur, 1, numbers, target)
    
    return answer
