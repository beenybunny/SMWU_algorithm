''' 
원형의 집들. 원형일 경우, 직선을 구해서 원형으로 바꿔준다.
d[i][j]
1번집과 n번집 고려 - 1번집의 색상을 미리 정해놓은 다음, 다이나믹을 3번 수행해서 정답을 구할 수 있다.
'''
n = int(input())
maxx = 1000*1000+1
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

d = [[0]*3 for _ in range(n)]
ans = maxx
for k in range(3): # house 1's color
    for j in range(3): # house1에 초기값 부여
        if j == k: # house1의 color면 정상적으로 a 부여
            d[0][j] = a[0][j]
        else: # house1과 다르다면 maxx부여하여 답이 되지 않도록.
            d[0][j] = maxx

    for i in range(1, n):
        d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
        d[i][2] = min(d[i-1][1], d[i-1][0]) + a[i][2]

    for j in range(3): # last house
        if j != k: # house 1과 색깔이 다를 때만
            ans = min(ans, d[n-1][j])

print(ans)

