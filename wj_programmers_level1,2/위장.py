def solution(clothes):
    answer = 0
    clo_hash = {}
    for c in clothes:
        if c[1] in clo_hash:
            clo_hash[c[1]] += 1
        else:
            clo_hash[c[1]] = 1
    
    clist = list(clo_hash.values())
    if len(clist) == 1:
        return clist[0]
    
    before = clist[0]
    answer = clist[0]
    for i in range(1,len(clist)):
        now = clist[i] + clist[i]*before
        answer += now
        before += now
        
    
    return answer


'''
ex.
[1,2,3,4] 
단순하게 나열하면, (1+2+3+4)+(1*2+1*3+1*4+2*3+2*4+3*4)+(1*2*3+1*2*4+1*3*4+2*3*4)+1*2*3*4

for문으로 계산하기 위해,
각 항이 추가될 때마다 더해지는 형식
1+(2+2*1)+(3+3*5)+(4+4*23)
'''
