def solution(brown, yellow):
    answer = []
    '''
    전체 격자 수 = brown + yellow
    전체 격자 수 = x*y (전체격자수의 약수들x,y)
    (x-2)*(y-2) = yellow
    (x*y)- yellow = brown
    완탐이랬으니까... 
    '''
    quantity = brown+yellow
    
    for i in range(quantity-2,2,-1): #quantity-2에서 3까지 
        if quantity%i ==0:
            for j in range(i,2,-1):
                if i * j == quantity and (i-2)*(j-2)== yellow:
                    answer.append(i)
                    answer.append(j)
                    return answer
    return answer