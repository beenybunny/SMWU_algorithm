def is_balanced(ww):
    right,left=0,0
    for w in ww:
        if w == '(':
            left += 1
        elif w== ')':
            right += 1
    if right == left:
        return True
    else:
        return False
def is_right(ww):
    left, right = 0,0
    for w in ww:
        if w == '(':
            left += 1
        elif w == ')':
            right += 1
        if left < right:
            return False
    return True

def seperate(w): 
    right, left = 0,0 # 2.
    for i in range(0,len(w)):
        if w[i] == '(':
            left += 1
        elif w[i] == ')':
            right += 1
        if left == right:
            u = w[:i+1]
            v = w[i+1:]
            return u,v
        
def solution(w):
    if w == '':
        return ''
    u,v = seperate(w)
    if is_right(u) == True:
        newv = solution(v)
        return u + newv
    elif is_right(u) == False:
        newv = solution(v)
        uu=u[1:-1]
        newu=''
        for i in uu:
            if i=='(':
                newu += ')'
            else:
                newu += '('
                
        return '('+ newv +')'+ newu
    
    '''
    간략하게 먼저 흐름 잡은 뒤에 코딩 시작하기
    def solution(w):
      if w='': return '' # 1.
      w->seperate(u,v) # 2.
      if is_right(u) == True: # 3.
          solution(v)
          return u+newv
      elif is_right(u) == False: # 4.
          u->newu 
          return '('+solution(v)+')'+newu
    '''
