import sys
input = sys.stdin.readline # 한줄 읽음
t = int(input())
for _ in range(t):
    sen = input() # s : 입력으로 들어오는 한 문장(한줄)
    stack = []
    for s in sen:
        if s == ' ' or s == '\n': # s가 띄어쓰기나 \n일때, stack 거꾸로 출력
            stack = stack[::-1]
            print(''.join(stack))
            stack.clear()  
        else: 
            stack.append(s)
        
