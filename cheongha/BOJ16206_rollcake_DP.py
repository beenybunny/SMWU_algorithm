roll_n, cut_n = map(int, input().split())
rolls_l = list(map(int, input().split()))

rolls_l.sort()

not_ten_l =[]
ans = 0

def cut(l):
    global ans
    global cut_n
    if (cut_n <= 0) : return
    else:
        l -= 10
        ans += 1
        cut_n -= 1
        if l > 10 :
            cut(l)
        elif l == 10 :
            ans +=1
        return
    
for i in range(roll_n):
    if cut_n <= 0 : break
    elif rolls_l[i] == 10 : ans += 1
    elif rolls_l[i] % 10 == 0 :
        cut(rolls_l[i])
    elif rolls_l[i] >10 :
        not_ten_l.append(rolls_l[i])
for i in range(len(not_ten_l)):
    cut(not_ten_l[i])
    
print(ans)
