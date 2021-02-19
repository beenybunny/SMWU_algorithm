'''
def solution(orders, course):
    answer = []
    order_comb = {}
    for order in orders:
        length = len(order)
        
        for i in range(length-1):
            base_menu = order[i]
            
            for j in range(i+1,len(order)):
                
                comb = base_menu+order[j]
                comb = tuple(sorted(comb))
                
                if comb in order_comb.keys():
                    order_comb[comb]+=1
                else: 
                    order_comb[comb]=1
                              
    order_comb = sorted(order_comb.items(), key = lambda item: item[1], reverse=True)
    max_amount = order_comb[0][1]
    max_idx = 0

    print(order_comb)
        
    while order_comb[max_idx][1] == max_amount:
        answer.append(order_comb[max_idx][0][0]+order_comb[max_idx][0][1])
        #여기도 N에 따라서 고쳐야 함..
        max_idx+=1
    print(answer)
    return answer
'''
#dfs로, 조합 !!
import pdb

def generate_combination(order,sub_menu,course_amount):
    #pdb.set_trace()
    if len(sub_menu) == course_amount:
        #sub_menu_= tuple(sub_menu)
        sub_menu_ = ''.join(sub_menu)
        
        if sub_menu_ in order_comb_dict.keys():
            order_comb_dict[sub_menu_] +=1
        else: order_comb_dict[sub_menu_] = 1
        #print(order_comb_dict)
        return 

    #start = order.index(sub_menu[-1]) +1 if sub_menu else 0 
    #==>list가 비어있으면 False값..인거 아닌데 왜 이렇게 되는거지?

    start = 0
    if len(sub_menu) > 0:
        start = order.index(sub_menu[-1])+1 #마지막
    for i in range(start,len(order)):
        sub_menu.append(order[i])
        generate_combination(order,sub_menu,course_amount)

        sub_menu.pop()
        
                             
def solution(orders, course):
    answer = []
    global order_comb_dict
    order_comb_dict = {}
    
    for c in course:
        for order in orders:
            order = sorted(order)
            generate_combination(order,[],c)
     
        if order_comb_dict:
            order_comb_dict = sorted(order_comb_dict.items(), key = lambda item: item[1], reverse=True)
            #print(order_comb_dict)
            max_amount = order_comb_dict[0][1]

            if max_amount >=2:
                for i in order_comb_dict:
                    if i[1] == max_amount :
                        answer.append(i[0])
                        
        order_comb_dict = {}
    print(sorted(answer))
    #print(order_comb_dict)

    
        
        
        
                
         

orders=["XYZ", "XWY", "WXA"]
course=[2,3,4]
solution(orders,course)
