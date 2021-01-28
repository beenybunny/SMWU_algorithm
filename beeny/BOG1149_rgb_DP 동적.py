import sys

def solution(n,costs):
    dp =[[0 for j in range(3)] for i in range(n)]
    i=0

    dp[i][0] = costs[i][0]
    dp[i][1] = costs[i][1]
    dp[i][2] = costs[i][2]

    #for i in range(len(costs)-1,-1,-1):
    for i in range(1,len(costs)):
        dp[i][0] = costs[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    #어떤 list를  참조해야하는지 똑바로 생각하기

    print(dp)
    print (min(dp[-1]))

if __name__ == "__main__":
    n = int(input())
    costs = [[] for i in range(n)]

    for i in range(n):
        costs[i].extend(map(int,sys.stdin.readline().split()))

    solution(n,costs)
