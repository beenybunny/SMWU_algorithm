n = int(input())

arr = []
arr = [0] + arr
before = 1
after = 1
dif = 0
ans = []

for i in range(1, 200001):
    arr.append(i*i)

while(True):
    if after >= len(arr):
        break
    dif = arr[after] - arr[before]
    
    if dif < n:
        after = after + 1
    if dif > n:
        before = before + 1
    if dif == n:
        ans.append(after)
        after = after + 1

if ans:
    for i in range(len(ans)):
        print(ans[i])
else:
    print(-1)
