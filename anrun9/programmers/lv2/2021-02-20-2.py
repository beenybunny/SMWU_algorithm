# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    for i in range(1, n):
        j = (i-1)*(i)//2
        if (n-j)//i < 1:
            break
        elif (n-j)%i == 0:
            answer+= 1
                
    return answer
