import sys
input = sys.stdin.readline # 한줄 읽음
n = int(input())
stack = []
for _ in range(n): # 변수가 별 의미 없을 때 _ 사용
    s = input().split()
    var = s[0]
    if var == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif var == 'size':
        print(len(stack))
    elif var == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif var == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif var == 'push':
        num = int(s[1])
        stack.append(num)
