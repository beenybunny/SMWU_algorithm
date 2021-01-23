def solution(prices):
    answer = []
    for i in range(0, len(prices)-1):
        a = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                a += 1
            else:
                a += 1
                break
        answer.append(a)
    answer.append(0)
    
    ''' while len(prices) != 0:
        a = 0
        f = prices.pop(0) 
        # pop이 시간이 오래걸려서 시간 초과뜸. 왜냐면 pop하고 재배열하기 때문에. 
        # 지금 while, pop, for가 중첩으로 되어 시간초과 뜨는 것. 차라리 이중for문이 낫다.
        for price in prices:
            a += 1
            if f > price:
                break
        answer.append(a)
        
        '''
        
    return answer
