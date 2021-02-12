# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = [strings[0]]
    for word in strings[1:]:
        for idx, inner in enumerate(answer):
            if word[n] < inner[n]:
                answer.insert(idx, word)
                break
            elif word[n] == inner[n]:
                if word < inner:
                    answer.insert(idx, word)
                    break
        else:
            answer.append(word)
    return answer
