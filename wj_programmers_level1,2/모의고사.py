def solution(answers):
    answer = []
    dic = {'1':0, '2':0, '3':0}
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    
    for i in range(0, len(answers)):
        if answers[i] == p1[i%5]:
            count[0] += 1
        if answers[i] == p2[i%8]:
            count[1] += 1
        if answers[i] == p3[i%10]:
            count[2] += 1
            
    for c in range(0,3):
        if count[c] == max(count):
            answer.append(c+1)
    
    return answer

# 다른 사람 풀이 보니 enumerate 활용하기 좋은 문제
