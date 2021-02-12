def solution(N, stages):
    #n이 스테이지 개수임, stages에는 현재 도전중인 스테이지 번호,  n+1있으면 끝까지 클리어
    reaching=[0 for i in range(N)] #i번째 스테이지에 도달 한 사람의 수. 
    trying = [0 for i in range(N)] #i번째 스테이지에 머물러있는(성공못한) 사람의 수 
    failure_rate = [0 for i in range(N)]
    
    for i in stages:
    #1부터 i까지 스테이지에 도달한 거임. 1부터 i-1까지 클리어한거임. 
        try :
            for j in range(i):
                reaching[j]+=1
        except IndexError as Succeed: #i>N 끝까지 도달한 사람.
            continue    
        
        trying[i-1] +=1 
    
    for i in range(N):
        try: failure_rate[i]= trying[i]/reaching[i]
        except:pass
    
    answer = {i:failure_rate[i] for i in range(N)}
    answer = sorted(answer.items(),reverse=True,key=lambda item: item[1])#값을 기준으로 내림차순
    
    stage_desc= []
    for i in range(N):
        stage_desc.append(answer[i][0]+1)
    return stage_desc
    
#정렬하고 스테이지 번호 출력하는 거 주의! -> list to dict 
#리팩토링 하기.. 처음부터 dict로 해야하나? 
