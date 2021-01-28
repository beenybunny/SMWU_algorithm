def solution(s):
    answer = 0
    #if isinstance(s[0],str):
    #OR if type(s[0])== str: 아 어짜피 문자열로 들어오니까 못 씀
    if s[0] == "+" :
        answer = int(s[1:])
    elif s[0] =="-":
        answer = int(s[1:]) *-1
    else: 
        answer = int(s)
        
    return answer