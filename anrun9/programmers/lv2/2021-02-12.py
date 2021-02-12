# 정렬
# H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse = True)
    h = citations[0]
    while True:
        answer = 0
        for i in citations:
            if i >= h:
                answer+= 1
            else:
                break
        if answer >= h:
            return h
        h-=1
