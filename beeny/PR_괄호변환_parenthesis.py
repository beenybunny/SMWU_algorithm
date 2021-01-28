'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
 v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.

'''

def solution(p):
    answer = ""

    if len(p) == 0: #1번
        return answer

    U,V = divide(p) #2

    if check_whether_its_right(U) :#3
        if len(V) >= 1:
            V= solution(V)
        return U+V

    else : #4
        return not_right(U,V)

def check_whether_its_right(U):
    #올바른 괄호 문자열인지 확인. ->
    stack = []
    stack.append(U[0])

    for i in range(1,len(U)) :
        if(stack[-1]=="(" and U[i]== ")"):
            stack.pop()
        else :stack.append(U[i])
    if len(stack) == 0 :
        return True
    else:
        return False

def not_right(U,V):
    ans = "("
    ans += solution(V)
    ans += ")"
    U = U[1:-1]

    for i in U :
        if(i == "("):
            ans+=")"
        else : ans+="("
    return ans

def divide(p):
    U = ""
    i = 0
    left_count = 0
    right_count = 0

    for i in range(len(p)):
        if p[i] == "(":
            left_count += 1
            U += p[i]

        elif p[i] == ")":
            right_count += 1
            U += p[i]

        #p = p[1:]  # 앞에 글자 하나 자르기,,이걸하면안되지;;

        if left_count == right_count:
            break

    return U,p[i+1:]

print(solution("()))((()"))