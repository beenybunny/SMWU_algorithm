import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pre_sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    pre_sum[i] = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, n+1):
        pre_sum[i][j] += pre_sum[i][j-1] + pre_sum[i-1][j] - pre_sum[i-1][j-1]

for i in range(m):
    a, b, c, d = map(int, input().split())
    ans = pre_sum[c][d] - pre_sum[a-1][d] - pre_sum[c][b-1] + pre_sum[a-1][b-1]
    print(ans)
