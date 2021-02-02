import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

a = 0
b = 0
ans = 0
ij_sum = 0

while(True):
    if (ij_sum >= m):
        ij_sum = ij_sum - l[a]
        a = a + 1
    elif b == n:
        break
    else:
        ij_sum = ij_sum + l[b]
        b = b + 1
    if ij_sum == m:
        ans = ans + 1

print(ans)
