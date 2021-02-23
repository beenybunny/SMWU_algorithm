# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0]*(len(prices))
    stack = []
    for idx, price in enumerate(prices):
        while stack:
            if stack[-1][0] > price:
                a, b = stack.pop()
                answer[b] = idx-b
            else:
                break
        stack.append((price, idx))
        stack.sort()
    
    while stack:
        a, b = stack.pop()
        answer[b] = len(prices) - b -1
        
    return answer
