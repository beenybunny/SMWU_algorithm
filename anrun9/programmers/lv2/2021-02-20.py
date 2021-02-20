# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = 0
    
    for i in s:
        if i == '(':
            answer+=1
        else:
            answer-=1
        if answer < 0:
            return False
    if answer == 0:
        return True
    return False
