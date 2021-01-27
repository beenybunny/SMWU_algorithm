N = int(input())
MOD = 1000000007

# N행 3열인 2차원 배열
dp = [[0]*3 for _ in range(N)]

dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 1

# dp[자릿수][3으로 나눴을 때 나머지(=3의 배수가 되기 위해서 필요한 수)]
for n in range(1, N):
    dp[n][0] = dp[n-1][2] + dp[n-1][1]
    dp[n][1] = dp[n-1][0] + dp[n-1][2]
    dp[n][2] = dp[n-1][1] + dp[n-1][0]
    
print(dp[N-1][0]%MOD)
