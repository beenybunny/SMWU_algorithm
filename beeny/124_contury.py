def solution(n):
    answer = ''
    #3진수 이용. 3으로 나누었을 때 나머지가 0일 때, 몫에서 1을 빼고 나머지를 4로 바꾼다
    quotient = n 
    while quotient > 0:
        remainder = quotient % 3  #나머지
        quotient = quotient // 3 #몫
        if remainder == 0 : 
            quotient -= 1
            remainder = 4
        answer+= str(remainder)                
    return answer[::-1]

if __name__ == "__main__":

    if solution(6)=="14": print("Correct")
    
