# 푸는 중
# 아래 반례들 모두 통과하는데 도대체 왜 testcase는.. 틀리는 반례를 찾고싶다..

import heapq
# heapq : 리스트를 최소 힙처럼 다룸. 일반 queue보다 훨씬 빠르다.
# 최소 힙 : 맨 앞의 원소가 최솟값
def solution(scv, K):
    answer = 0
    if K == 0:
        return 0
    while len(scv) > 1:
        min1 = heapq.heappop(scv)
        min2 = heapq.heappop(scv)
        num = min1 + min2 * 2
        heapq.heappush(scv, num)
        answer += 1
        
        if scv[0] >= K:
            return answer
        
    return -1
    
'''
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)
'''
