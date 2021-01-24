def solution(a, b):
    answer = ''
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"] 
    dnum = b
    i = a-1
    # 총 일수 dnum
    while i != 0:
        i -= 1
        dnum += date[i]
    
    # 요일 
    dnum %= 7
    answer = day[(4+dnum)%7]
    
    return answer
