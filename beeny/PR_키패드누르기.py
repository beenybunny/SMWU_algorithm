def index_num_loc(num):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for i in range(len(keypad)):
        try:
            a = keypad[i].index(num)
            return (i,a)
        except: pass

def left(left_idx,num_idx):
    i = left_idx[0]
    j = left_idx[1]
    
    i_move = abs(left_idx[0]-num_idx[0])
    j_move = abs(left_idx[1]-num_idx[1])
    
    return i_move+j_move

def right(right_idx,num_idx):
    i = right_idx[0]
    j = right_idx[1]
    
    i_move = abs(right_idx[0]-num_idx[0])
    j_move = abs(right_idx[1]-num_idx[1])
    
    return i_move+j_move
def solution(numbers, hand):
    #20210128
    answer = ''
    left_idx = (3,0) # * 왼손 시작점
    right_idx = (3,2) # # 오른쪽 시작점

    for num in numbers:
        num_idx = index_num_loc(num)
                
        if num in (1,4,7):
            left(left_idx,num_idx)
            left_idx = num_idx
            answer += "L"
            
        elif num in (3,6,9):
            right(right_idx,num_idx)
            right_idx = num_idx
            answer += "R"
            
        else:
            left_num= left(left_idx,num_idx)
            right_num= right(right_idx,num_idx)
            
            if left_num> right_num : 
                answer +="R"
                right_idx = num_idx
            elif right_num > left_num : 
                answer+="L"
                left_idx = num_idx
                
            else: #같은 경우 
                if hand=="right":
                    answer += "R"
                    right_idx = num_idx
                else:
                    answer+="L"
                    left_idx = num_idx
    return answer

#중복되는 코드가 많은 것 같음! 리팩토링 하기 


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers,hand))
    #answer = "LRLLLRLLRRL"
