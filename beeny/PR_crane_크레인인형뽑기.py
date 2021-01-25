import pdb

def solution (board,moves):
    items = []
    pop = 0
    i=[0 for i in range(len(board))]
    
    #pdb.set_trace()
    for move in moves:
        j = move-1

        if i[j] >= len(board):
            continue
        
        item = board[i[j]][j]
        #i[j] +=1

        while item == 0 :
            if i[j]+1 >= len(board): #board[0]으로 하면 n*n에 안맞을듯? 아근데 nn이라 ㄱㅊ을듯,, 
                break
            i[j] +=1
            item = board[i[j]][j]

        if (len(items) == 0 or items[-1] != item):
            items.append(item)

        elif (items[-1] == item):
            items.pop()
            pop+=2

        print(items)
        i[j]+=1
    
    '''
        
        if(board[i][-1] !=0):
            #print("item",board[i][-1],"items",items)
            if(len(items) == 0 or items[-1] != board[i][-1]):
                items.append(board[i].pop())
            else:
                items.pop()
                pop += 2 
    ''' 
    print(pop)

if __name__ =="__main__":
    #solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])
    solution([[0,0,1],[1,2,3],[3,1,2]],[3,1,2,1,2,3,1,2,3])
