def solution(array, commands):
    answer = []
    for com in commands:
        arr = array
     #   i = com[0]; j = com[1]; k = com[2] 
        i,j,k = com
        arr = arr[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    
    return answer
'''
 return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
모범답안에 이렇게 한줄로 표현한 멋진 사람도 있었다. 지나치게 줄이는 건 의미가 없긴 하지만 
lambda, map은 공부해야겠다.
 '''
