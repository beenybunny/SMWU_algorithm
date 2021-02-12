# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for i in list(s):
        if ord(i) == 32:
            answer += ' '
        else:
            if 65 <= ord(i) <= 90-n or 97 <= ord(i) <= 122-n :
                answer += chr(ord(i)+n)
            else:
                answer += chr(ord(i)+n-26)
            
    return answer
