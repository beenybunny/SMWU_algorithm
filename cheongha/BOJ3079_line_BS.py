import sys
input = sys.stdin.readline
n,m = map(int, input().split())
line = []
for i in range(n):
    line.append(int(input()))

right = 10**18
left = 1
ans = right
while right >= left:
    mid = (left + right) // 2
    s = 0
    for i in range(n):
        s += mid // line[i]
        if s >= m:
            break
    if s >= m:
        if mid < ans:
            ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
