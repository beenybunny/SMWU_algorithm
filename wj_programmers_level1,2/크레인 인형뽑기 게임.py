def solution(board, moves):
    answer = 0
    bnum = len(board)
    list = []
    for m in moves:
        # decide out number
        for i in range(0, bnum):
            out = board[i][m-1]
            if out == 0:
                continue
            else:
                board[i][m-1] = 0 # put 0 in that position
                list.append(out) # append out in list
                break
    
    # list - 여기서 헤매는 중
    leng = len(list)
    l = -1
    while l != leng-2 and l != -2:
        l = l+1
        if list[l] == list[l+1]:
            answer = answer + 2
            del list[l]
            del list[l]
            leng = leng-2
            l = l-2
            
        else:
            continue
    
    return answer
