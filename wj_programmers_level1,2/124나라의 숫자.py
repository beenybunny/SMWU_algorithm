# 첫 시도 - testcase 일부 통과못함 & 효율성 X
'''
# 진법 변환 문제와 유사
def solution(n):
    answer = '1'
    rest = []
    while n > 0: # 10진수 -> 3진수
        r = n % 3
        n //= 3
        rest.append(r)
    rest.reverse()
    
    # 3진수 -> 124나라
    # 1) 3진수 -> 123나라
    if 0 not in rest:
        rest = rest
    # 0 처리 
    elif 0 in rest:
        for i in range(0, len(rest)):
            if rest[i] == 0:
                rest[i-1] -= 1
                rest[i] = 3
                
    # 2) 123나라 -> 124나라
    # replace는 string에서만! list에서는 불가능
    # ** convert int list to string ** 1.int->str 2. combine str
    
    rest = [str(integer) for integer in rest]
    str_rest = ''.join(rest)
    answer = int(str_rest) # 맨앞의 0 제거하기 위함
    answer = str(answer) 
    answer = answer.replace('3','4')

    return answer
'''

# 모범 답안 보고 다시
def solution(n):
    answer = ''
    q = n
    # 10진수->3진수 변환. 이때 나머지가 0이면 4로 변환 후, 남은 몫에 -1.
    while q > 0: # q = 몫, r = 나머지
        r = q % 3
        q = q //3
        if r == 0:
            r = 4
            q -= 1
        answer += str(r)
    print(answer)
    return answer[::-1]
