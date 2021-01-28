def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    #print(participant)
    #print(completion)
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    #print(answer)
    if answer == '':
        answer = participant[-1]
    return answer