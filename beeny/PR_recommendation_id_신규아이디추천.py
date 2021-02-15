answer = ''
new_id = "...!@BaT#*..y.abcdefghijklm"
print(new_id)
# 1
new_id = new_id.lower()

new_id = list(new_id)
#반복문에서 list remove할때 무조건 주의해야함..

# 2
count = 0
length  = len(new_id)
while len(new_id) > 0 and count < length:
    i = new_id[count]
    if i.isdigit() or i.isalpha() or i == "-" or i == "_" or i == ".":
        count+=1
    else:
        new_id.remove(i)
        #remove됐을 때 count를 늘리면 안됨. 문자 하나 넘어감
        length = len(new_id)
# 3
#for문 돌릴때 list length쓰는데 지우면서 하면 out of range.날수도 있지 ! while도, 조건문에 쓰는 len은 고정인가봄
print(new_id)
if len(new_id) > 1:
    #for i in range(1, len(new_id)):
    count = 1
    length = len(new_id)
    while len(new_id) > 1 and count < length:
        if new_id[count] == "." and new_id[count - 1] == ".":
            del new_id[count]
            length = len(new_id)
        else:
            count+=1

# 4
if len(new_id) > 0:
    if new_id[0] == ".":
        del new_id[0]
if len(new_id) > 0:
    if new_id[-1] == ".":
        del new_id[-1]

# 5
if len(new_id) == 0:
    new_id.append("a")
# 6
if len(new_id) > 15:
    new_id = new_id[:15] #16이 아니라 15였음
if new_id[-1] == ".":
    del new_id[-1]
# 7
if len(new_id) < 3:
    while len(new_id) < 3:
        new_id.append(new_id[-1])

answer = "".join(new_id)
print(answer)
