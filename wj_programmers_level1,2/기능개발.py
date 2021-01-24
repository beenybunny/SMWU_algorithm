import math
def solution(progresses, speeds):
    answer = []
    work = []
    for i in range(0, len(progresses)):
        work.append( math.ceil((100-progresses[i])/speeds[i]) )
    
    prev = work[0]
    a = 1
    for i in range(1, len(work)):
        if prev >= work[i]:
            a += 1
        else:
            answer.append(a)
            a = 1
            prev = work[i]
    answer.append(a)
    
    return answer


 # 처음엔 pop()을 이용하려했지만, 이 방식대로면 바로 근접한 원소끼리만 비교하기 때문에 안된다는 걸 깨달음.
  #  추가된 반례를 통과못함. 앞에서부터 for문으로 해야할듯.
   
