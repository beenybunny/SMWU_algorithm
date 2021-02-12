# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    for i in range(min(n, m), 0, -1):
        if all(map(lambda x: x%i==0, [n, m])):
            return [i, n*m//i]
