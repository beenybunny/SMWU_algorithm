while True:
    s = input()
    if s == ".":
        break
    stk = []
    ans = True

    for i in s:
        if i == "(" or i == "[":
            stk.append(i)
            
        if i == ")":
            if not stk:
                ans = False
                break
            elif stk[-1] == "(":
                stk.pop()
            else:
                ans = False
                break
            
        if i == "]":
            if not stk:
                ans = False
                break
            if stk[-1] == "[":
                stk.pop()
            else:
                ans = False
                break

    if ans == True and not stk:
        print("yes")
    else:
        print("no")
