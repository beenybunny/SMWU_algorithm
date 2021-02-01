import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pre_sum = list(map(int, input().split()))

for i in range(1, n):
    pre_sum[i] = pre_sum[i-1] + pre_sum[i]
pre_sum = [0] + pre_sum

for i in range(m):
    a, b = map(int, input().split())
    print(pre_sum[b] - pre_sum[a-1])
