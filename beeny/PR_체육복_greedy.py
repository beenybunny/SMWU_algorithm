def solution(n, lost, reserve):
    answer = 0
    student = n-len(lost) #체육 수업 들을 수 있는 학생 수 
    length = len(lost)
    i = -1
    
    while True: #마지막 요구사항 맞추려고 이거 추가한거! 
        i+=1
        if i>=len(lost): break
        if lost[i] in reserve:
            reserve.remove(lost[i])#인덱스로 지우면 안됨; lost랑 reserve의 length가 다르니까 
            #del lost[i] 
            lost.remove(lost[i])
            student +=1
            i-=1
    #배열 원소 삭제하면서 for문 도는거 (in len(list) 일때) 불가능. -> 방법을 찾아보자 
             
    for i in range(len(lost)):
        who_lost = lost[i]
        if who_lost-1 in reserve: 
                reserve.remove(who_lost-1)
        elif who_lost+1 in reserve: 
                reserve.remove(who_lost+1)    
        else: continue
        student+=1
    return student
    
#왜 자꾸 마지막껏만 틀리는거야,, 5번 제약사항위배
#(여분있는애가 도난당하면 다른사람한테 아예 빌려줄 수 없음..) 3,[1,2][2,3]했을 때 2나와야 함.
#-> 일단 여분있는 애중에 도난당한애가 있는지부터 봐야할듯
