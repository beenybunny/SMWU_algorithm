# 피보나치수
# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    Fi = [0, 1]
    while len(Fi) < (n+1):
        Fi.append(Fi[-2] + Fi[-1])
    
    return Fi[-1]%1234567
